from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.item_line import Item_line
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models.seasoning import Seasoning
from ebookstore_flask.models.shipping import Shipping
from ebookstore_flask import db

from datetime import date

user_discount = Blueprint('user_discount', __name__)

@user_discount.route('/user/profile/discount')
def index():
    print('test')
    def check_availability(discount):
        discount_type = discount.Disc_type
        if discount_type == 'Seasoning':
            disc_seasoning = Seasoning.query.filter_by(DID=discount.DID).first()
            valid_to = disc_seasoning.Valid_to
            valid_from = disc_seasoning.Valid_from
            if date.today() <= valid_to and date.today() >= valid_from:
                return True
            else :
                return False
        elif discount_type == 'Special Event':
            disc_special = Special_event.query.filter_by(DID=discount.DID).first()
            valid_to = disc_special.Valid_to
            valid_from = disc_special.Valid_from
            if date.today() <= valid_to and date.today() >= valid_from:
                return True
            else :
                return False
        return True
    
    def check_used(discount, member_id):
        used = []
        orders = Order.query.filter_by(CMID=member_id).first()
        for order in orders:
            if order.DID and order.DID==discount.DID:
                return True
        return False

    session_now = load_sessions()
    key = list(session_now.keys())[0]
    email = session_now[key][0]
    member = Member.query.filter_by(Email=email).first()
    member_id = member.MID

    used = []
    available = []
    expired = []

    discounts = Discount.query.all()
    for discount in discounts:
        if check_availability(discount):
            available.append(discount)
        else:
            expired.append(discount)

        if check_used(discount, member_id):
            used.append(discount)
    print('expired:', expired)
        
    return render_template('/user/discount.html')

    