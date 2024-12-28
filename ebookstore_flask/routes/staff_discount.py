from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask import db

staff_discount = Blueprint('staff_discount', __name__)

@staff_discount.route('/staff/discount')
def index(type="", returned="main"):
    def format_product_data(discount):
        return {
        "DID": discount.DID,
        "Disc_code": discount.Disc_code,
        "Disc_value": 100 - int(discount.Disc_value * 100),
        "Disc_type": discount.Disc_type
    }

    def filter_ordered_products(list, discount_type):
        status_map = {
        "discount": ["Shipping","Seasoning","Special Event"],
        "shipping": ["Shipping"],
        "seasoning": ["Seasoning"],
        "specialEvent": ["Special Event"]
        }
        filtered_discount = []
        for line in list:
            if not discount_type or line.Disc_type in status_map.get(discount_type, []):
                filtered_discount.append(format_product_data(line))
        return filtered_discount
    check_role("Staff", "Administrator")

    discount = Discount.query.all()
    discount_list = filter_ordered_products(discount,type)
    discount_list.sort(key=lambda x: x["DID"])

    print("discount_list",discount_list)

    if returned == "find":
        return discount_list

    # all_items = [list(values) for values in grouped_data.values()]
    active_route = type or "discount"
    return render_template(f"/staff/discount.html", all_items=discount_list, active_route=active_route)

@staff_discount.route('/staff/discount/shipping')
def shipped():
   return index("shipping")

@staff_discount.route('/staff/discount/seasoning')
def finished():
   return index("seasoning")

@staff_discount.route('/staff/discount/specialEvent')
def returned():
   return index("specialEvent")

@staff_discount.route('/<path:current_path>/findDiscount', methods=['POST'])
def filter_by(current_path):
    user_input = request.form.get('user_input', "").strip() 
    filter_field = request.form.get('filter_field', "discount_id")

    type_info = current_path.split('/')
    current_type = type_info.pop()

    data = index(type=current_type, returned="find")

    filtered_items = []
    
    for item in data:
        print("DID",item['DID'])
        print("filter_field",filter_field)
        print("user_input",user_input)
        print(filter_field == "discountID")
        print(user_input.isdigit())
        print(item['DID'] == user_input)
        if filter_field == "discountID" and user_input.isdigit() and item['DID'] == int(user_input):
            print("msk sini")
            filtered_items.append(item)
        elif filter_field == "discountCode":
            if user_input.lower() in item["Disc_code"].lower():
                filtered_items.append(item)
            
    print("filtered_items",filtered_items)
    return render_template(
        "/staff/discount.html",
        all_items=filtered_items,
        user_input=user_input,
        filter_field=filter_field,
        active_route=current_type
    )
