from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
def index():
   from ebookstore_flask.models.product import Product
   from ebookstore_flask.models.review import Review
   from ebookstore_flask import db
   # .all() must be added in all query
   # it used to convert SQL query object into python list
   best_seller = (
      Product.query                         # SELECT * FROM "Product"
      .order_by(Product.Sale_count.desc())  # ORDER BY "Sale_count" DESC
      .limit(10)                            # LIMIT 10;
      .all()
   )
   
   new_release = (
      Product.query                  # SELECT * FROM "Product"
      .order_by(Product.PID.desc())  # ORDER BY "PID" DESC
      .limit(10)                     # LIMIT 10;
      .all()
   )
   
   top_5_category = (
      Product.query.with_entities(Product.Category)      # SELECT "Category" FROM "Product"
      .group_by(Product.Category)                        # GROUP BY "Category"
      .order_by(db.func.sum(Product.Sale_count).desc())  # ORDER BY SUM("Sale_count")
      .limit(5)                                          # LIMIT 5;
      .all()
   )
   top_5_category = [category[0] for category in top_5_category]  # because query result is [(category1,), (category2,), (category3,)]
   
   top_rated = (
      db.session.query(Product, Review.Rate) # SELECT "Product".*, "Review"."Rate" FROM "Product", "Review"
      .filter(Product.PID == Review.PID)     # WHERE "Product"."PID" = "Review"."PID"
      .filter(Review.Rate.isnot(None))       #   AND "Review"."Rate" IS NOT NULL
      .order_by(Review.Rate.desc())          # ORDER BY "Review"."Rate" DESC
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
   
   return render_template(
      "/user/home.html",
      best_seller=best_seller,
      new_release=new_release,
      top_5_category=top_5_category,
      top_rated=top_rated
   )
