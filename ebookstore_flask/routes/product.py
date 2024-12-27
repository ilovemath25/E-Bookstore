from flask import Blueprint, render_template

product = Blueprint('product', __name__)

@product.route('/book/<int:product_id>')
def index(product_id):
   from ebookstore_flask.models.product import Product
   product = Product.query.get(product_id)
   if product:
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
   return render_template(
      "/user/product.html",
      product=product
   )