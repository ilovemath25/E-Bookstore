'''
Generates SQL INSERT statements from all database models and writes them to a file.
'''
from ebookstore_flask import create_app, db
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.credit_card import Credit_card
from ebookstore_flask.models.shoppingCart_item import ShoppingCart_item
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.seasoning import Seasoning
from ebookstore_flask.models.shipping import Shipping
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models.review import Review

def format_value(value):
   if isinstance(value, str): return f"'{value}'"
   elif value is None: return 'NULL'
   elif isinstance(value, bool): return 'TRUE' if value else 'FALSE'
   else: return str(value)

def generate_insert_statements():
   models = [Member, Credit_card, Discount, Shipping, Seasoning, Special_event, Order, Product, ShoppingCart_item, Item_line, Review]
   with open('output_query.txt', 'w', encoding='utf-8') as file:
      for model in models:
         table_name = model.__tablename__
         columns = [column.name for column in model.__table__.columns]
         rows = db.session.query(model).all()
         if rows:
            file.write(f'INSERT INTO "{table_name}" ({", ".join(columns)})\nVALUES\n')
            values_list = []
            for row in rows:
               values = [format_value(getattr(row, column)) for column in columns]
               values_list.append(f"  ({', '.join(values)})")
            file.write(",\n".join(values_list) + ";\n\n")

if __name__ == "__main__":
   POSTGRES = {
      'user':'postgres',
      'password':'thiha2001',
      'db':'postgres',
      'host':'localhost',
      'port':'5432',
   }
   app = create_app(POSTGRES)
   with app.app_context(): generate_insert_statements()