from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.review import Review
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.shoppingCart_item import ShoppingCart_item
from ebookstore_flask.models import db

product = Blueprint('product', __name__)

@product.route('/book/<int:product_id>')
def index(product_id):
   product = Product.query.get(product_id)
   reviews = Review.query.filter_by(PID=product_id).all()
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   def format_review_data(review):
      member = Member.query.filter_by(MID=review.MID).all()
      return {
         "PID": review.PID,
         "MID": review.MID,
         "FName": member[0].F_name,
         "LName": member[0].L_name,
         "Time": review.Time,
         "Rate": review.Rate,
         "Text": review.Rev_text
      }
   review_detail=[]
   for review in reviews:
      review_detail.append(format_review_data(review))
   return render_template(
      "/user/product.html",
      product=product,
      reviews=review_detail,
      role=role
   )
   
@product.route('/book/<int:product_id>/add_cart')
def add_cart(product_id):
   product = Product.query.get(product_id)
   session_data = check_session()
   email = session_data[0]
   member = Member.query.filter_by(Email=email).first()
   customer_ID = member.MID
   itemLine = (
      Item_line.query
      .filter_by(PID=product_id)
      .join(ShoppingCart_item, ShoppingCart_item.SCID == Item_line.SCID)
      .filter(ShoppingCart_item.CMID==customer_ID)
      .filter(Item_line.Line_type == 'ShoppingCart')
      .first()
   )
   if itemLine :
      shopCartID = itemLine.SCID
      itemLine.Quantity = itemLine.Quantity + 1
      shoppingCart = ShoppingCart_item.query.filter_by(SCID = shopCartID).first()
      shoppingCart.Tot_price = product.Price * itemLine.Quantity
      db.session.commit()
   else:
      new_shopCart = ShoppingCart_item(
         CMID = customer_ID,
         Tot_price = product.Price
      )
      db.session.add(new_shopCart)
      db.session.commit()
      new_itemline = Item_line(
         PID = product.PID,
         SCID = new_shopCart.SCID,
         Line_type = "ShoppingCart",
         Quantity = 1
      )
      db.session.add(new_itemline)
      db.session.commit()
   return redirect(url_for('product.index', product_id=product_id))