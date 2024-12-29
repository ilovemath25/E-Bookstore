from flask import Blueprint, render_template

product = Blueprint('product', __name__)

@product.route('/book/<int:product_id>')
def index(product_id):
   from ebookstore_flask.models.product import Product
   product = Product.query.get(product_id)
   return render_template(
      "/user/product.html",
      product=product
   )