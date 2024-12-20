from flask import Flask
from ebookstore_flask.models import db
def create_app(postgres):
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'YourSecretKey'
   app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{postgres['user']}:{postgres['password']}@{postgres['host']}:{postgres['port']}/{postgres['db']}"
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   db.init_app(app)
   with app.app_context():
      from ebookstore_flask.routes.home import home
      from ebookstore_flask.routes.product import product
      from ebookstore_flask.routes.login import login
      from ebookstore_flask.routes.staff_order import staff_order
      from ebookstore_flask.routes.staff_order_detail import staff_order_detail
      from ebookstore_flask.routes.staff_discount_detail import staff_discount_detail
      app.register_blueprint(home)
      app.register_blueprint(login)
      app.register_blueprint(product)
      app.register_blueprint(staff_order)
      app.register_blueprint(staff_order_detail)
      app.register_blueprint(staff_discount_detail)

   return app