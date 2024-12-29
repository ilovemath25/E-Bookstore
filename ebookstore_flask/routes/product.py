from flask import Blueprint, render_template
from ebookstore_flask.utils.session import check_session

product = Blueprint('product', __name__)

@product.route('/book/<int:product_id>')
def index(product_id):
   from ebookstore_flask.models.product import Product
   product = Product.query.get(product_id)
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      "/user/product.html",
      product=product,
      role=role
   )