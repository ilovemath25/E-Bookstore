from flask import Blueprint, render_template

staff_order = Blueprint('staff_order', __name__)

@staff_order.route('/staff_order')
def index():
   from ebookstore_flask.models.order import Order
   from ebookstore_flask.models.item_line import Item_line
   from ebookstore_flask.models.product import Product
   from ebookstore_flask import db

   from itertools import groupby

   item_lines = Item_line.query.filter(Item_line.Line_type == "Order").all()
   
   ordered_product = []
   for line in item_lines:
      product = (Product.query.filter(line.PID == Product.PID).all())
      product = product[0]

      order = (Order.query.filter(line.OID == Order.OID).all())
      order = order[0]
      
      #later will refactor using sum in order
      #price * quantity
      sum_price = line.Quantity * product.Price
      # if product.Product_pict.startswith('ebookstore_flask/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '')
      # if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')

      ordered_product.append({"product_pic": product.Product_pict,"Name" : product.Name,"Quantity": line.Quantity, "Sum" : sum_price, "OID": line.OID, "CMID": order.CMID, "Status": order.Status})
   

   ordered_product.sort(key=lambda x: x["OID"])
   grouped_data = {key: list(value) for key, value in groupby(ordered_product, key=lambda x: x["OID"])}

   all_items = []
   for key, values in grouped_data.items():
      save = []
      for val in values:
         save.append(val)
      all_items.append(save)
   
   print(all_items)


   # for order in all_orders:
   #    if order.Product.Product_pict.startswith('ebookstore_flask/'):order.Product.Product_pict = order.Product.Product_pict.replace('ebookstore_flask/', '')
   #    if order.Product.Product_pict.startswith('static/'):order.Product.Product_pict = order.Product.Product_pict.replace('static/', '')

   return render_template("/staff/order.html", all_items=all_items)