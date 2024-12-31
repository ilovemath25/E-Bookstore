from flask import Blueprint, render_template
from ebookstore_flask.utils.session import check_session

product = Blueprint('product', __name__)

@product.route('/book/<int:product_id>')
def index(product_id):
   from ebookstore_flask.models.product import Product
   from ebookstore_flask.models.review import Review
   from ebookstore_flask.models.member import Member
   product = Product.query.get(product_id)
   reviews = Review.query.filter_by(PID=product_id).all()
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
      print(type(review.Rate))
      review_detail.append(format_review_data(review))
   print(review_detail)
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      "/user/product.html",
      product=product,
      reviews=review_detail,
      role=role
   )