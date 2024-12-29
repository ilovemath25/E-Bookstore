from flask import Flask
import pandas as pd, os
from ebookstore_flask.models import db
def create_app(postgres):
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'YourSecretKey'
   app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{postgres['user']}:{postgres['password']}@{postgres['host']}:{postgres['port']}/{postgres['db']}"
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   bin_data = pd.read_csv(os.path.join(os.getcwd(), "binlist.csv"))
   app.config['BIN_DATA'] = bin_data
   db.init_app(app)
   @app.context_processor
   def inject_global_data():
      from ebookstore_flask.models.product import Product
      search_dataset = Product.query.with_entities(Product.Name).all()
      search_dataset = [data[0] for data in search_dataset]
      return {"search_dataset": search_dataset}
   with app.app_context():
      from ebookstore_flask.routes.home import home
      from ebookstore_flask.routes.product import product
      from ebookstore_flask.routes.login import login
      from ebookstore_flask.routes.staff_order import staff_order
      from ebookstore_flask.routes.staff_discount import staff_discount
      from ebookstore_flask.routes.staff_order_detail import staff_order_detail
      from ebookstore_flask.routes.staff_discount_detail import staff_discount_detail
      from ebookstore_flask.routes.staff_discount_add import staff_discount_add
      from ebookstore_flask.routes.user_profile import user_profile
      from ebookstore_flask.routes.staff_centre import staff_centre
      from ebookstore_flask.routes.book_list import book_list
      from ebookstore_flask.routes.error import error
      from ebookstore_flask.routes.staff_product import staff_product
      from ebookstore_flask.routes.staff_product_detail import staff_product_detail
      from ebookstore_flask.routes.staff_product_add import staff_product_add
      app.register_blueprint(home)
      app.register_blueprint(login)
      app.register_blueprint(product)
      app.register_blueprint(staff_order)
      app.register_blueprint(staff_discount)
      app.register_blueprint(staff_order_detail)
      app.register_blueprint(staff_discount_detail)
      app.register_blueprint(staff_discount_add)
      app.register_blueprint(user_profile)
      app.register_blueprint(staff_centre)
      app.register_blueprint(book_list)
      app.register_blueprint(error)
      app.register_blueprint(staff_product)
      app.register_blueprint(staff_product_detail)
      app.register_blueprint(staff_product_add)
   return app