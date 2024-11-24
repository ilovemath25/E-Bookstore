from flask import Flask, render_template
from models import db
from models.member import Member
from models.product import Product
from models.item_line import Item_line
from models.shoppingCart_item import ShoppingCart_item
from models.order import Order
from models.discount import Discount
from models.special_event import Special_event
from models.seasoning import Seasoning
from models.shipping import Shipping
from models.review import Review
from models.credit_card import Credit_card
app = Flask(__name__)
POSTGRES = {
   'user':'postgres',
   'password':'ilovemath25',
   'db':'ebookstore',
   'host':'localhost',
   'port':'5432',
}
app.config['SECRET_KEY'] = 'YourSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{POSTGRES['user']}:{POSTGRES['password']}@{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
   members = Member.query.all()
   return render_template("main.html", members=members)
if __name__=='__main__': app.run(debug=True, port=5000)
