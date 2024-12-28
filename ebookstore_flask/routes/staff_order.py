from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask import db

from itertools import groupby

staff_order = Blueprint('staff_order', __name__)

@staff_order.route('/staff/order')
def index(order_type="order", returned="main"):
   print("current_type1",order_type)
   def format_product_data(line, product, order):
      sum_price = line.Quantity * product.Price
      product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '').replace('static/', '')
      return {
         "Product_pict": product.Product_pict,
         "Name": product.Name,
         "Quantity": line.Quantity,
         "Sum": sum_price,
         "OID": line.OID,
         "CMID": order.CMID,
         "Status": order.Status
      }

   def filter_ordered_products(item_lines, order_type):
      status_map = {
         "order": ["Processing","Closed","Shipping", "Received", "Returned", "Cancel"],
         "to_ship": ["Processing"],
         "finished": ["Closed", "Received"],
         "returned": ["Returned", "Cancel"]
      }
      filtered_products = []
      for line in item_lines:
         product = Product.query.filter_by(PID=line.PID).first()
         order = Order.query.filter_by(OID=line.OID).first()
         if not order_type or order.Status in status_map.get(order_type, []):
            filtered_products.append(format_product_data(line, product, order))
      return filtered_products
   check_role("Staff", "Administrator")

   item_lines = Item_line.query.filter_by(Line_type="Order").all()
   ordered_product = filter_ordered_products(item_lines, order_type)
   print("ordered_product",ordered_product)
   ordered_product.sort(key=lambda x: x["OID"])
   grouped_data = {key: list(value) for key, value in groupby(ordered_product, key=lambda x: x["OID"])}

   if returned == "find":
      print("find msk sini")
      return grouped_data

   all_items = [list(values) for values in grouped_data.values()]
   active_route = order_type
   print("current_type",active_route)
   return render_template("/staff/order.html", all_items=all_items, active_route=active_route)

@staff_order.route('/staff/order/to_ship')
def shipped():
   return index("to_ship")

@staff_order.route('/staff/order/finished')
def finished():
   return index("finished")

@staff_order.route('/staff/order/returned')
def returned():
   return index("returned")

@staff_order.route('/<path:current_path>/findOrder', methods=['POST'])
def filter_by(current_path):
      user_input = request.form.get('user_input', "").strip() 
      filter_field = request.form.get('filter_field', "order_id")

      type_info = current_path.split('/')
      current_type = type_info.pop()

      data = index(order_type=current_type, returned="find")
      print("current_type",current_type)
      filtered_items = []
      for key, values in data.items():
         if filter_field == "order_id" and user_input.isdigit() and str(key) == user_input:
            filtered_items.append(values)
         elif filter_field == "product":
            filtered_values = [val for val in values if user_input.lower() in val["Name"].lower()]
            if filtered_values:
                  filtered_items.append(values)
      
      return render_template(
         "/staff/order.html",
         all_items=filtered_items,
         user_input=user_input,
         filter_field=filter_field,
         active_route=current_type

)
