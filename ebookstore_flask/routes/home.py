from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
def index():
   from ebookstore_flask.models.product import Product
   best_seller = Product().query.order_by(Product.Sale_count.desc()).limit(10).all()
   new_release = Product().query.order_by(Product.PID.desc()).limit(10).all()
   for product in best_seller:
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
   for product in new_release:
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
   return render_template("home.html", best_seller=best_seller, new_release=new_release)