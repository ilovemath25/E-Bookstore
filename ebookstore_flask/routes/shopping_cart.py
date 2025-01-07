from flask import Blueprint, request, redirect, url_for, render_template, jsonify, session
from ebookstore_flask.utils.session import check_session, load_sessions
from ebookstore_flask.utils.credit_card import bin_number_checker
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.credit_card import Credit_card
from ebookstore_flask.models.shoppingCart_item import ShoppingCart_item
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.order import Order
from ebookstore_flask.models import db
from datetime import datetime

shopping_cart = Blueprint('shopping_cart', __name__)

@shopping_cart.route('/cart')
def index(buyNow=""):
   buyNow = request.args.get('buyNow', '')
   session_data = check_session()
   if not session_data: return redirect(url_for('login.index'))
   email = session_data[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                      # SELECT * FROM "Member"
      .filter(Member.Email == email)    # WHERE "Email" = email
      .first()
   )
   cards = (
      Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
      .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
      .filter(Member.Email == email)                      # WHERE "Member"."Email" = <email>;
      .all()
   )

   if buyNow:
      product = Product.query.get(buyNow)
      member = Member.query.filter_by(Email=email).first()
      customer_ID = member.MID
      new_shopCart = ShoppingCart_item(
         CMID = customer_ID,
         Tot_price = product.Price
      )
      db.session.add(new_shopCart)
      db.session.commit()

      new_itemline = Item_line(
         PID = product.PID,
         SCID = new_shopCart.SCID,
         Line_type = "Order",
         Quantity = 1
      )
      db.session.add(new_itemline)
      db.session.commit()

   products = (
      Product.query                                                       # SELECT * FROM "Product"
      .join(Item_line, Item_line.PID == Product.PID)                      # JOIN "Item_line" ON "Item_line"."PID" = "Product"."PID"
      .join(ShoppingCart_item, ShoppingCart_item.SCID == Item_line.SCID)  # JOIN "ShoppingCart_item" ON "ShoppingCart_item"."CMID" = "Item_line"."SCID"
      .filter(ShoppingCart_item.CMID == user.MID)                         # WHERE "ShoppingCart_item"."CMID" = user.MID
      .all()
   )

   credit_cards = [card[0] for card in cards]
   for i in range(len(credit_cards)):
      bin_info = bin_number_checker(credit_cards[i][:6])
      credit_cards[i] = '**** **** **** ' + credit_cards[i][-4:]
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   try:
      buyNow = int(buyNow)
   except:
      buyNow = buyNow
   discount_code = session.get('discount_code')
   discount = None
   if discount_code: discount = Discount.query.filter(Discount.Disc_code == discount_code).first()
   discount_message = session.pop('discount_message', '')
   card_message = session.pop('card_message', '')
   return render_template(
      'user/shopping_cart.html',
      role=session_data[1],
      products=products,
      credit_cards=credit_cards,
      buyNow=buyNow,
      discount=discount,
      dmsg=discount_message,
      cmsg=card_message
   )

@shopping_cart.route('/cart/apply_discount', methods=['POST'])
def apply_discount():
   discount_code = request.form.get('discount_code')
   discount = (
      Discount.query                                # SELECT * FROM "Discount"
      .filter(Discount.Disc_code == discount_code)  # WHERE "Code" = discount_code
      .first()
   )
   if not discount:
      session['discount_code'] = discount_code
      session['discount_message'] = 'invalid'
   else:
      session['discount_code'] = discount_code
      session['discount_message'] = 'success'
   return redirect(url_for('shopping_cart.index'))

@shopping_cart.route('/cart/add_card', methods=['POST'])
def add_card():
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   if request.method == 'POST':
      number = request.form.get('Number')
      expiry = request.form.get('Expiry')
      cvv = request.form.get('CVV')
      expiry_date = datetime.strptime(f"01/{expiry}", "%d/%m/%y").date()
      
      # Check if the card already exists
      existing_card = Credit_card.query.filter(Credit_card.Number == number).first()
      if existing_card:
         session['card_message'] = 'Card already exists'
         return redirect(url_for('shopping_cart.index'))
      
      card = Credit_card(
         Number=number,
         Expiry_date=expiry_date,
         CVV=cvv,
         CMID=Member.query.with_entities(Member.MID).filter(Member.Email == email).first()[0]
      )
      db.session.add(card)
      db.session.commit()
      return redirect(url_for('shopping_cart.index'))

def check_all_cart(user):
   carts = (
      ShoppingCart_item.query
      .filter(ShoppingCart_item.CMID == user.MID)
      .all()
   )
   for cart in carts:
      item_line = (
         Item_line.query
         .filter(Item_line.SCID == cart.SCID)
         .first()
      )
      if item_line is None: db.session.delete(cart)
   db.session.commit()

@shopping_cart.route('/cart/delete', methods=['POST'])
def delete():
   pid = request.form.get('pid')
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                      # SELECT * FROM "Member"
      .filter(Member.Email == email)    # WHERE "Email" = email
      .first()
   )
   item_line = (
      Item_line.query                                                     # SELECT * FROM "Item_line"
      .join(ShoppingCart_item, ShoppingCart_item.SCID == Item_line.SCID)  # JOIN "ShoppingCart_item" ON "ShoppingCart_item"."SCID" = "Item_line"."SCID"
      .filter(ShoppingCart_item.CMID == user.MID)                         # WHERE "ShoppingCart_item"."CMID" = "Member"."MID"
      .filter(Item_line.PID == int(pid))                                  #   AND "Item_line"."PID" = <pid>
      .first()
   )
   db.session.delete(item_line)
   db.session.commit()
   check_all_cart(user)
   return redirect(url_for('shopping_cart.index'))

@shopping_cart.route('/cart/checkout', methods=['POST'])
def checkout():
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   data = request.json
   products = data.get('products', [])
   payment_method = data.get('paymentMethod')
   selected_card_index = data.get('selectedCardIndex', None)
   address = data.get('address', {})
   total_price = data.get('totalPrice')
   user = (
      Member.query                      # SELECT * FROM "Member"
      .filter(Member.Email == email)    # WHERE "Email" = email
      .first()
   )
   selected_card = None
   if payment_method == 'Credit card':
      cards = (
         Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
         .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
         .all()
      )
      selected_card = cards[selected_card_index][0]
   else: pass
   
   discount_code = session.get('discount_code')
   discount = None
   if discount_code: discount = Discount.query.filter(Discount.Disc_code == discount_code).first()
   
   new_order = Order(
      CMID=user.MID,
      SMID=2,
      DID=discount.DID if discount else None,
      Credit_num=selected_card,
      Time=datetime.now(),
      Ship_address=address['Address'],
      Ship_fee=30,
      Status='Processing',
      Pay_method=payment_method,
      Tot_price=total_price
   )
   db.session.add(new_order)
   db.session.flush()
   for product in products:
      pid = product['id']
      quantity = product['quantity']
      item_line = (
         Item_line.query                                                     # SELECT * FROM "Item_line"
         .join(ShoppingCart_item, ShoppingCart_item.SCID == Item_line.SCID)  # JOIN "ShoppingCart_item" ON "ShoppingCart_item"."SCID" = "Item_line"."SCID"
         .filter(ShoppingCart_item.CMID == user.MID)                         # WHERE "ShoppingCart_item"."CMID" = "Member"."MID"
         .filter(Item_line.PID == pid)                                       #   AND "Item_line"."PID" = <pid>
         .first()
      )
      item_line.Quantity = quantity
      item_line.OID = new_order.OID
      item_line.SCID = None
      item_line.Line_type = "Order"
   db.session.commit()
   if 'discount_code' in session: session.pop('discount_code')
   return jsonify({
      'message': 'Order placed successfully!',
      'order_id': new_order.OID
   })