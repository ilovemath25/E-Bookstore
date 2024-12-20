from flask import Blueprint, render_template

staff_order = Blueprint('staff_order', __name__)

@staff_order.route('/staff_order')
def index():
   return render_template("/staff/order.html")