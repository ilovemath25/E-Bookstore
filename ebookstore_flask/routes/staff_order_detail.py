from flask import Blueprint, render_template

staff_order_detail = Blueprint('staff_order_detail', __name__)

@staff_order_detail.route('/staff_order/detail')
def index():
   return render_template("/staff/order_detail.html")