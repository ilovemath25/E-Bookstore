from flask import Blueprint, render_template

staff_order_detail = Blueprint('staff_order_detail', __name__)

@staff_order_detail.route('/staff/order_detail/<int:order_id>')
def index(order_id):
   from ebookstore_flask.models.order import Order
   from ebookstore_flask.models.member import Member
   from ebookstore_flask.models.item_line import Item_line
   from ebookstore_flask.models.product import Product
   from ebookstore_flask.models.discount import Discount
   from ebookstore_flask.models.special_event import Special_event

   order = Order.query.get(order_id)
   customer = Member.query.get(order.CMID) if order else None
   item_lines = Item_line.query.filter_by(OID=order_id).all()
   discounts = Discount.query.get(order.DID) if order else None

   item_details = []
   total_price = 0
   for line in item_lines:
      product = Product.query.get(line.PID)
      prt_price = product.Price
      if discounts and product.SpEvent_ID==order.DID:
         prt_price *= discounts.Disc_value
      subtotal = line.Quantity * prt_price
      total_price += subtotal
      if product and product.Product_pict:
         if product.Product_pict.startswith('ebookstore_flask/static/'):product.Product_pict = product.Product_pict.replace('ebookstore_flask/static/', '')
         if product.Product_pict.startswith('static/'):product.Product_pict = product.Product_pict.replace('static/', '')
      item_details.append({"line": line, "product": product, "prt_price":prt_price, "subtotal": subtotal})

   shp_fee = order.Ship_fee
   if discounts and discounts.Disc_type=='Shipping':
      shp_fee *= discounts.Disc_value

   order_total = shp_fee + total_price
   if discounts and discounts.Disc_type=='Seasoning':
      order_total = round(order_total * discounts.Disc_value)
      order_total = int(order_total)
   
   steps = [
      {"status": "Processing", "text": "Order Made", "completed_statuses": ["Processing", "Shipping", "Received", "Closed"], "line_completed_statuses": ["Shipping", "Received", "Closed"]},
      {"status": "Shipping", "text": "Sent to be shipped", "completed_statuses": ["Shipping", "Received", "Closed"], "line_completed_statuses": ["Received", "Closed"]},
      {"status": "Received", "text": "Arrived at receiving address", "completed_statuses": ["Received", "Closed"], "line_completed_statuses": ["Closed"]},
      {"status": "Closed", "text": "Collected by customer", "completed_statuses": ["Closed"], "line_completed_statuses": []},
   ]

   return render_template(
      "/staff/order_detail.html", 
      order=order, 
      customer=customer, 
      item_details=item_details, 
      total_price=total_price, 
      shp_fee=shp_fee, 
      order_total=order_total, 
      steps=steps
   )
