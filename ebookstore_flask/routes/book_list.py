from flask import Blueprint, render_template, request
from ebookstore_flask.utils.session import check_session

book_list = Blueprint('book_list', __name__)

@book_list.route('/category/<string:category_name>')
def category(category_name):
   from ebookstore_flask.models.product import Product
   book_list = (
      Product.query                        # SELECT * FROM "Product"
      .filter_by(Category = category_name) # WHERE "Category" = <category_name>;
      .all()
   )
   for book in book_list:
      if book.Product_pict.startswith('ebookstore_flask/'):book.Product_pict = book.Product_pict.replace('ebookstore_flask/', '')
      if book.Product_pict.startswith('static/'):book.Product_pict = book.Product_pict.replace('static/', '')
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      "user/book_list.html",
      category_name=category_name,
      book_list=book_list,
      role=role,
      is_category=True,
   )

@book_list.route('/book')
def all_book():
   from ebookstore_flask.models.product import Product
   all_list = (
      Product.query           # SELECT * FROM "Product"
      .order_by(Product.Name) # ORDER BY "Name";
      .all()
   )
   book_list={}
   for product in all_list:
      first_letter = product.Name[0].upper()
      if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
      if first_letter not in book_list:book_list[first_letter] = []
      book_list[first_letter].append(product)
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      "user/book_list.html",
      book_list=book_list,
      is_all_book=True,
      role=role
   )

@book_list.route('/search/<string:user_search>')
def search(user_search):
   from ebookstore_flask.models.product import Product
   from ebookstore_flask.utils.search import search_books
   all_list = (
      Product.query           # SELECT * FROM "Product"
      .order_by(Product.Name) # ORDER BY "Name";
      .all()
   )
   results = search_books(user_search, all_list)
   book_list = []
   for book in results:
      if book.Product_pict.startswith('ebookstore_flask/'):book.Product_pict = book.Product_pict.replace('ebookstore_flask/', '')
      if book.Product_pict.startswith('static/'):book.Product_pict = book.Product_pict.replace('static/', '')
      book_list.append(book)
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      "user/book_list.html",
      book_list=book_list,
      user_search=user_search,
      is_search=True
   )