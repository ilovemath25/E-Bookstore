from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.order import Order
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models.seasoning import Seasoning
from ebookstore_flask.models.shipping import Shipping
from ebookstore_flask import db

from datetime import date

user_discount = Blueprint('user_discount', __name__)

@user_discount.route('/discount')
def index():
    def check_availability(discount):
        if not discount:
            return False
        if discount.Disc_type == 'Shipping':
            return True
        if discount.Valid_from and discount.Valid_to:
            valid_from = discount.Valid_from
            valid_to = discount.Valid_to
        if valid_to and valid_from <= date.today() <= valid_to:
            return True
        return False

    def check_used(discount, member_id):
        orders = Order.query.filter_by(CMID=member_id).all()
        return any(order.DID == discount.DID for order in orders)

    
    session_data = check_session()
    if not check_session():
        return redirect(url_for('login.index'))
    session_id = request.cookies.get("session_id")
    sessions = load_sessions()
    email = sessions.get(session_id, [None])[0]  
    if not email: return redirect(url_for('login.index'))
    member = Member.query.filter_by(Email=email).first()
    member_id = member.MID

    used = []
    available = []
    expired = []

    discounts = (
        db.session.query(
            Discount.DID,
            Discount.Disc_code,
            Discount.Disc_value,
            Discount.Disc_type,
            Discount.Disc_name,
            Discount.Policy_desc,
            Discount.Max_usage,
            db.func.coalesce(Seasoning.Valid_from, Special_event.Valid_from).label('Valid_from'),
            db.func.coalesce(Seasoning.Valid_to, Special_event.Valid_to).label('Valid_to'),
            Shipping.Min_purchase.label('Shipping_Min_purchase'),
        )
        .outerjoin(Seasoning, Seasoning.DID == Discount.DID)
        .outerjoin(Shipping, Shipping.DID == Discount.DID)
        .outerjoin(Special_event, Special_event.DID == Discount.DID)
        .all()
    )
    for discount in discounts:
        
        if check_availability(discount):
            available.append(discount)
        else:
            expired.append(discount)
        if check_used(discount, member_id):
            used.append(discount)
    
    return render_template(
        '/user/discount.html',
        available=available,
        used=used,
        expired=expired,
        role=session_data[1] if session_data else None
    )