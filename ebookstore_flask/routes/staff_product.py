from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask import db

from itertools import groupby

staff_product = Blueprint('staff_product', __name__)

@staff_product.route('/staff/product')
def index(type="", returned="main"):
    def format_product_data(product):
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
    check_role("Staff", "Administrator")

    product = Product.query.all()
    product_list = filter_ordered_products(product,type)
    product_list.sort(key=lambda x: x["PID"])
    print(product_list)

    if returned == "find":
        return product_list

    active_route = type or "product"
    return render_template(f"/staff/product.html", all_items=product_list, active_route=active_route)

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
    for item in data:
            print("filter_field",filter_field)
            if filter_field == "product_id" and user_input.isdigit() and item['PID'] == int(user_input):
                filtered_items.append(item)
            elif filter_field == "product_name":
                if user_input.lower() in item["Name"].lower():
                    filtered_items.append(item)
            elif filter_field == "category":
                if user_input.lower() in item["Category"].lower():
                    filtered_items.append(item)
            
    print("filtered_items",filtered_items)
    return render_template(
        "/staff/product.html",
        all_items=filtered_items,
        user_input=user_input,
        filter_field=filter_field,
        active_route=current_type
    )
