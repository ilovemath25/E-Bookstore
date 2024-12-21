from flask import Blueprint, redirect, render_template, request
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask import db

from itertools import groupby

staff_order = Blueprint('staff_order', __name__)

@staff_order.route('/staff_order')
def index(type="",returned="main"):
   item_lines = Item_line.query.filter(Item_line.Line_type == "Order").all()
   
   ordered_product = []
   for line in item_lines:
      product = (Product.query.filter(line.PID == Product.PID).all())
      product = product[0]

      order = (Order.query.filter(line.OID == Order.OID).all())
      order = order[0]
      
      if type=="":
         #later will refactor using sum in order
         #price * quantity
         sum_price = line.Quantity * product.Price
         if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
         if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
         ordered_product.append({"Product_pict": product.Product_pict,"Name" : product.Name,"Quantity": line.Quantity, "Sum" : sum_price, "OID": line.OID, "CMID": order.CMID, "Status": order.Status})
      elif type=="to_ship":
         if order.Status == "Processing":
            #later will refactor using sum in order
            #price * quantity
            sum_price = line.Quantity * product.Price
            if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
            if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
            ordered_product.append({"Product_pict": product.Product_pict,"Name" : product.Name,"Quantity": line.Quantity, "Sum" : sum_price, "OID": line.OID, "CMID": order.CMID, "Status": order.Status})
      elif type=="finished":
         if order.Status == "Closed" or order.Status == "Received":
            #later will refactor using sum in order
            #price * quantity
            sum_price = line.Quantity * product.Price
            if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
            if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
            ordered_product.append({"Product_pict": product.Product_pict,"Name" : product.Name,"Quantity": line.Quantity, "Sum" : sum_price, "OID": line.OID, "CMID": order.CMID, "Status": order.Status})
      elif type=="returned":
         if order.Status == "Returned" or order.Status == "Cancel":
            #later will refactor using sum in order
            #price * quantity
            sum_price = line.Quantity * product.Price
            if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
            if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
            ordered_product.append({"Product_pict": product.Product_pict,"Name" : product.Name,"Quantity": line.Quantity, "Sum" : sum_price, "OID": line.OID, "CMID": order.CMID, "Status": order.Status})
      if type == "staff_order":
         # 添加處理邏輯或報錯提示
         return render_template("/staff/order.html", all_items=[], active_route="staff_order")




      
   
   ordered_product.sort(key=lambda x: x["OID"])
   grouped_data = {key: list(value) for key, value in groupby(ordered_product, key=lambda x: x["OID"])}

   if returned=="find":
      return grouped_data

   all_items = []
   for key, values in grouped_data.items():
      save = []
      for val in values:
         save.append(val)
      all_items.append(save)

   if type=="":
      return render_template("/staff/order.html", all_items=all_items,active_route="main")
   elif type=="to_ship":
      return render_template("/staff/order.html", all_items=all_items,active_route="to_ship")
   elif type=="finished":
      return render_template("/staff/order.html", all_items=all_items,active_route="finished")
   elif type=="returned":
      return render_template("/staff/order.html", all_items=all_items,active_route="returned")
   return render_template("/staff/order.html", all_items=all_items)

@staff_order.route('/staff_order/to_ship')
def shipped():
   return index("to_ship")

@staff_order.route('/staff_order/finished')
def finished():
   return index("finished")

@staff_order.route('/staff_order/returned')
def returned():
   return index("returned")


@staff_order.route('/<path:current_path>/find', methods=['POST'])
def filter_by(current_path):
      user_input = request.form.get('user_input', "").strip() 
      filter_field = request.form.get('filter_field', "order_id")
      if not user_input:
        return redirect(f"/{current_path}")
      
      type_info = current_path.split('/')
      current_type = type_info[1] if len(type_info) > 1 else None

      data = index(type=current_type, returned="find")

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






   