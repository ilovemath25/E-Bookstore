from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask import db

from itertools import groupby

staff_product = Blueprint('staff_product', __name__)

@staff_product.route('/staff/product')
def index(type="", returned="main"):
    def format_product_data(product):
        product.Product_pict = product.Product_pict.replace('ebookstore_flask/', '').replace('static/', '')
        return {
        "PID": product.PID,
        "Name": product.Name,
        "Author": product.Author,
        "Category": product.Category,
        "Price": product.Price,
        "Product_pict": product.Product_pict,
        "Stock": product.Stock_quantity
    }

    def filter_ordered_products(list, product_type):
        filtered_product = []
        for line in list:
            if product_type == "outofstock" and line.Stock_quantity == 0:
                filtered_product.append(format_product_data(line))
            elif product_type == "product" or not product_type:
                filtered_product.append(format_product_data(line))
        return filtered_product
    if check_session(): 
        session_id = request.cookies.get("session_id")
        sessions = load_sessions()
        email = sessions.get(session_id, [None])[0]
        role = sessions.get(session_id, [None])[1]
        if not email: return redirect(url_for('login.index'))
        if role == 'Customer': return redirect(url_for('home.index'))

    product = Product.query.all()
    product_list = filter_ordered_products(product,type)
    product_list.sort(key=lambda x: x["PID"])
    grouped_data = {key: list(value) for key, value in groupby(product_list, key=lambda x: x["PID"])}

    # print("grouped_data",grouped_data)

    if returned == "find":
        return grouped_data

    all_items = [list(values) for values in grouped_data.values()]
    active_route = type or "product"
    return render_template(f"/staff/product.html", all_items=all_items, active_route=active_route)

@staff_product.route('/staff/product/outofstock')
def outofstock():
   return index("outofstock")

@staff_product.route('/<path:current_path>/findProduct', methods=['POST'])
def filter_by(current_path):
    user_input = request.form.get('user_input', "").strip() 
    filter_field = request.form.get('filter_field', "product_id")

    type_info = current_path.split('/')
    current_type = type_info.pop()
    print(f"Filter field: {filter_field}, User input: {user_input}, Current type: {current_type}")
    data = index(type=current_type, returned="find")

    filtered_items = []
    for key, items in data.items():
            print("filter_field",filter_field)
            if filter_field == "product_id" and user_input.isdigit() and str(key) == user_input:
                filtered_items.append(items)
            elif filter_field == "product_name":
                filtered_values = [val for val in items if user_input.lower() in val["Name"].lower()]
                if filtered_values:
                    filtered_items.append(items)
            elif filter_field == "category":
                filtered_values = [val for val in items if user_input.lower() in val["Category"].lower()]
                if filtered_values:
                    filtered_items.append(items)
            
    print("filtered_items",filtered_items)
    return render_template(
        "/staff/product.html",
        all_items=filtered_items,
        user_input=user_input,
        filter_field=filter_field,
        active_route=current_type
    )
