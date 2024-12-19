from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
def index():
   from ebookstore_flask.models.product import Product
   from ebookstore_flask.models.review import Review
   from ebookstore_flask import db
   best_seller = (
      Product.query
      .order_by(Product.Sale_count.desc())
      .limit(10)
      .all()
   )
   
   new_release = (
      Product.query
      .order_by(Product.PID.desc())
      .limit(10)
      .all()
   )
   
   top_5_category = (
      Product.query
      .with_entities(Product.Category)
      .group_by(Product.Category)
      .order_by(db.func.sum(Product.Sale_count).desc())
      .limit(5)
      .all()
   )
   top_5_category = [category[0] for category in top_5_category]
   
   top_rated = (
      db.session.query(Product, Review.Rate)
      .filter(Product.PID == Review.PID)
      .filter(Review.Rate.isnot(None))
      .order_by(Review.Rate.desc())
      .all()
   )
   
   for product in best_seller:
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
   for product in new_release:
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
   for product in top_rated:
      if product.Product.Product_pict.startswith('ebookstore_flask/'):product.Product.Product_pict = product.Product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product.Product_pict.startswith('static/'):product.Product.Product_pict = product.Product.Product_pict.replace('static/', '')
   
   return render_template("home.html",
      best_seller=best_seller,
      new_release=new_release,
      top_5_category=top_5_category,
      top_rated=top_rated
   )