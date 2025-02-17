from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions
from ebookstore_flask.utils.credit_card import bin_number_checker
from ebookstore_flask.models.credit_card import Credit_card
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.review import Review
from ebookstore_flask.models import db
from datetime import datetime
from itertools import groupby

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/user/profile')
def index():
   if not check_session(): return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      'user/user_profile.html',
      user=user,
      role=role
   )

@user_profile.route('/user/profile/edit', methods=['POST','GET'])
def edit():
   if not check_session(): return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   if request.method == 'POST':
      user.F_name = request.form.get('F_name')
      user.L_name = request.form.get('L_name')
      birth = request.form.get('Birth')
      user.Birth = birth if birth else None
      user.Gender = request.form.get('Gender')
      user.Email = request.form.get('Email')
      user.Phone = request.form.get('Phone')
      user.Address = request.form.get('Address')
      db.session.commit()
      return redirect(url_for('user_profile.index'))

   return render_template(
      'user/user_profile_edit.html',
      user=user,
      role=role
   )

@user_profile.route('/user/profile/credit_card')
def credit_card():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   cards = (
      Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
      .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
      .filter(Member.Email == email)                      # WHERE "Member"."Email" = <email>;
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
   return render_template(
      'user/user_profile_credit_card.html',
      credit_cards=credit_cards,
      role=session_data[1] if session_data else None
   )

@user_profile.route('/user/profile/credit_card/edit', methods=['POST', 'GET'])
def credit_card_edit():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   cards = (
      Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
      .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
      .filter(Member.Email == email)                      # WHERE "Member"."Email" = <email>;
      .all()
   )
   credit_cards = [card[0] for card in cards]
   for i in range(len(credit_cards)):
      bin_info = bin_number_checker(credit_cards[i][:6])
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   return render_template(
      'user/user_profile_credit_card_edit.html',
      credit_cards=credit_cards,
      role=session_data[1] if session_data else None
   )

@user_profile.route('/user/profile/credit_card/add', methods=['POST', 'GET'])
def credit_card_add():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   if request.method == 'POST':
      number = request.form.get('Number')
      expiry = request.form.get('Expiry')
      cvv = request.form.get('CVV')
      expiry_date = datetime.strptime(f"01/{expiry}", "%d/%m/%y").date()
      card = Credit_card(
         Number=number,
         Expiry_date=expiry_date,
         CVV=cvv,
         CMID=Member.query.with_entities(Member.MID).filter(Member.Email == email).first()[0]
      )
      db.session.add(card)
      db.session.commit()
      return redirect(url_for('user_profile.credit_card'))

@user_profile.route('/user/profile/credit_card/delete', methods=['POST', 'GET'])
def credit_card_delete():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   if request.method == 'POST':
      number = request.form.get('Number')
      card = Credit_card.query.filter_by(Number=number).first()
      db.session.delete(card)
      db.session.commit()
      return redirect(url_for('user_profile.credit_card'))

@user_profile.route('/user/profile/change_password', methods=['GET', 'POST'])
def change_password():
   session_data = check_session()
   if not check_session():
      return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email:
      return redirect(url_for('login.index'))

   from ebookstore_flask.models.member import Member
   from ebookstore_flask.models import db

   user = Member.query.filter_by(Email=email).first()
   if not user:
      return "User not found.", 404

   if request.method == 'POST':
      old_password = request.form.get('currentPassword')
      new_password = request.form.get('newPassword')
      confirm_password = request.form.get('confirmNewPassword')
      print(user.Password , old_password)

      user.Password = new_password
      db.session.commit()

      return redirect(url_for('user_profile.index'))

   return render_template(
      'user/user_profile_change_password.html',
      old_password=user.Password,
      role=session_data[1] if session_data else None
   )

@user_profile.route('/user/profile/order_history')
def order(order_type="order", returned="main"):
   if not check_session():
      return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email:
      return redirect(url_for('login.index'))
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   costumer_id = user.MID
   # print("current_type1",order_type)
   def format_product_data(line, product, order):
      sum_price = line.Quantity * product.Price
      return {
         "Product_pict": product.Product_pict,
         "Name": product.Name,
         "Quantity": line.Quantity,
         "Sum": sum_price,
         "OID": line.OID,
         "CMID": order.CMID,
         "Status": order.Status
      }
   def filter_ordered_products(item_lines, order_type):
      status_map = {
         "order": ["Processing","Closed","Shipping", "Received", "Returned", "Cancel"],
         "processing": ["Processing"],
         "shipping": ["Shipping"],
         "received": ["Received"],
         "closed": ["Closed"]
      }
      filtered_products = []
      for line in item_lines:
         product = Product.query.filter_by(PID=line.PID).first()
         order = Order.query.filter_by(OID=line.OID).first()
         if not order_type or order.Status in status_map.get(order_type, []):
            filtered_products.append(format_product_data(line, product, order))
      return filtered_products
   # check_role("Staff", "Administrator")
   item_lines = Item_line.query.filter_by(Line_type="Order").all()
   ordered_product = filter_ordered_products(item_lines, order_type)
   # print("ordered_product",ordered_product)
   ordered_product.sort(key=lambda x: x["OID"])
   grouped_data = {key: list(value) for key, value in groupby(ordered_product, key=lambda x: x["OID"])}
   
   filtered_grouped_data = {
      key: [item for item in value if item['CMID'] == costumer_id]
      for key, value in grouped_data.items()
      if any(item['CMID'] == costumer_id for item in value)  # Check for non-empty result
   }
   if returned == "find":
      return filtered_grouped_data
   all_items = [list(values) for values in filtered_grouped_data.values()]
   active_route = order_type if order_type != "order" else "order_history"
   return render_template(
      'user/user_profile_order_history.html',
      all_items=all_items,
      active_route=active_route,
      role=role
   )
@user_profile.route('/user/profile/order_history/processing')
def processing():
   return order(order_type="processing")
@user_profile.route('/user/profile/order_history/shipping')
def shipping():
   return order(order_type="shipping")
@user_profile.route('/user/profile/order_history/received')
def received():
   return order(order_type="received")
@user_profile.route('/user/profile/order_history/closed')
def closed():
   return order(order_type="closed")

@user_profile.route('/user/profile/order_history/<int:order_id>', methods=['GET', 'POST'])
def order_detail(order_id):
   print ("order_id",order_id)
   if not check_session():
      return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email:
      return redirect(url_for('login.index'))
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data

   order = Order.query.get(order_id)
   customer = Member.query.get(order.CMID) if order else None
   item_lines = Item_line.query.filter_by(OID=order_id).all()
   discounts = Discount.query.get(order.DID) if order else None

   item_details = []
   total_price = 0
   for line in item_lines:
      already_reviewed = False
      ReviewID = (
         db.session.query(Review.RID)
         .join(Item_line, Item_line.PID == Review.PID)
         .join(Order, Order.OID == Item_line.OID)
         .join(Member, Member.MID == Review.MID)
         .filter(Item_line.OID == order_id)
         .filter(line.PID == Review.PID)
         .first()
      )
      if ReviewID: already_reviewed = True
      product = Product.query.get(line.PID)
      prt_price = product.Price
      if discounts and product.SpEvent_ID==order.DID:
         prt_price *= discounts.Disc_value
      subtotal = line.Quantity * prt_price
      total_price += subtotal
      item_details.append({"line": line, "product": product, "prt_price":prt_price, "subtotal": subtotal, "customer": customer, "order": order, "alreadyRated": already_reviewed})

   shp_fee = order.Ship_fee
   if discounts and discounts.Disc_type=='Shipping':
      shp_fee *= discounts.Disc_value

   order_total = shp_fee + total_price
   if discounts and discounts.Disc_type=='Seasoning':
      order_total = round(order_total * discounts.Disc_value)
      order_total = int(order_total)
   
   steps = [
      {"status": "Processing", "text": "Processing", "completed_statuses": ["Processing", "Shipping", "Received", "Closed"], "line_completed_statuses": ["Shipping", "Received", "Closed"]},
      {"status": "Shipping", "text": "Shipping", "completed_statuses": ["Shipping", "Received", "Closed"], "line_completed_statuses": ["Received", "Closed"]},
      {"status": "Received", "text": "Arrived", "completed_statuses": ["Received", "Closed"], "line_completed_statuses": ["Closed"]},
      {"status": "Closed", "text": "Collected", "completed_statuses": ["Closed"], "line_completed_statuses": []},
   ]
   if request.method == 'GET':
      return render_template(
         "/user/user_profile_order_history_detail.html", 
         order=order, 
         customer=customer, 
         item_details=item_details, 
         total_price=total_price, 
         shp_fee=shp_fee, 
         order_total=order_total, 
         steps=steps,
         role=role
      )
   
@user_profile.route('/submit_rating', methods=['POST'])
def submit_rating():
   product_id = request.json.get('product_id') # Product ID
   rating = request.json.get('rating')         # Rating value
   review = request.json.get('review')         # Review text
   customer_id= request.json.get('customer_id')      

   add_review(int(product_id), int(customer_id), int(rating), review)

   # Process the data (e.g., save to a database)
   return f"Product ID: {product_id}, Rating: {rating}, Review: {review} submitted successfully!"

def add_review(product_id, member_id, rating, review_text):
   print(f"Product ID: {product_id}")
   print(f"Rating: {rating}")
   print(f"Review: {review_text}")
   print(f"Customer ID: {member_id}")
   try:
        # Create a new Review object
        new_review = Review(
            PID=product_id,
            MID=member_id,
            Time=datetime.now(),
            Rate=rating,
            Rev_text=review_text,
        )

        # Add to the session
        db.session.add(new_review)

        # Commit the session
        db.session.commit()

        print("Review added successfully!")
        return {"message": "Review added successfully!"}, 201

   except Exception as e:
        # Rollback in case of an error
        db.session.rollback()
        print(f"Error adding review: {e}")
        return {"error": str(e)}, 500