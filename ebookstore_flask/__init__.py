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
      app.register_blueprint(home)
   return app