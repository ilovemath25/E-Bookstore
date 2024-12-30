from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.discount import Discount
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models.shipping import Shipping
from ebookstore_flask.models.seasoning import Seasoning
from ebookstore_flask.models import db
from ebookstore_flask.utils.role import check_role
from datetime import datetime

staff_discount_detail = Blueprint('staff_discount_detail', __name__)

@staff_discount_detail.route('/staff/discount_detail/<int:discount_id>')
def index(discount_id):
    check_role("Staff", "Administrator")

    discount = Discount.query.filter_by(DID=discount_id).first()
    details = {}
    if discount.Disc_type == 'Seasoning':
        details = Seasoning.query.filter_by(DID=discount_id).first()
    elif discount.Disc_type == 'Special Event':
        details = Special_event.query.filter_by(DID=discount_id).first()
    elif discount.Disc_type == 'Shipping':
        details = Shipping.query.filter_by(DID=discount_id).first()

    return render_template(
        "/staff/discount_detail.html",
        discount=discount,
        details=details,
        discount_ID=discount_id
    )

@staff_discount_detail.route('/staff/discount_detail/<int:discount_id>/edit')
def index2(discount_id):
    from ebookstore_flask.models.discount import Discount
    from ebookstore_flask.models.special_event import Special_event
    from ebookstore_flask.models.shipping import Shipping
    from ebookstore_flask.models.seasoning import Seasoning

    check_role("Staff", "Administrator")

    errorMsg = request.args.get('errorMsg', '')

    discount = Discount.query.filter_by(DID=discount_id).first()
    details = {}
    if discount.Disc_type == 'Seasoning':
        details = Seasoning.query.filter_by(DID=discount_id).first()
    elif discount.Disc_type == 'Special Event':
        details = Special_event.query.filter_by(DID=discount_id).first()
    elif discount.Disc_type == 'Shipping':
        details = Shipping.query.filter_by(DID=discount_id).first()

    return render_template(
        "/staff/discount_detail_edit.html",
        discount=discount,
        details=details,
        discount_ID=discount_id,
        errorMsg=errorMsg
    )

@staff_discount_detail.route('/staff/discount_detail/<int:discount_id>/update', methods=['POST'])
def update_discount(discount_id):
    from ebookstore_flask import db
    from ebookstore_flask.models.discount import Discount
    from ebookstore_flask.models.special_event import Special_event
    from ebookstore_flask.models.shipping import Shipping
    from ebookstore_flask.models.seasoning import Seasoning

    discount = Discount.query.filter_by(DID=discount_id).first()

    Disc_code = request.form.get('Disc_code')
    Disc_value = request.form.get('Disc_value')

    #constraint
    discount_check = Discount.query.filter_by(Disc_code=Disc_code).first()
    if discount_check and (discount_check.DID != discount_id):
        return redirect(url_for('staff_discount_detail.index2',discount_id=discount_id,errorMsg="Discount Code already exists!"))
    
    if '.' not in Disc_value: 
        return redirect(url_for('staff_discount_detail.index2',discount_id=discount_id,errorMsg="Discount Value should be decimal!"))
    
    discount.Disc_name = request.form.get('Disc_name')
    discount.Disc_code = Disc_code
    discount.Policy_desc = request.form.get('Policy_desc')
    discount.Disc_type = request.form.get('Disc_type')
    discount.Disc_value = Disc_value
    discount.Max_usage = request.form.get('Max_usage')

    if discount.Disc_type == 'Shipping':
        details = Shipping.query.filter_by(DID=discount_id).first()
        Min_purchase = request.form.get('Min_purchase')
        if Min_purchase.isdigit() == False:
            return redirect(url_for('staff_discount_detail.index2',discount_id=discount_id,errorMsg="Minimal purchase should be number!"))
        else:
            details.Min_purchase = Min_purchase
    elif discount.Disc_type == 'Seasoning':
        details = Seasoning.query.filter_by(DID=discount_id).first()
        Valid_to = request.form.get('Valid_to')
        Valid_from = request.form.get('Valid_from')
        try:
            Valid_to = datetime.strptime(Valid_to, '%Y-%m-%d') if Valid_to else None
            Valid_from = datetime.strptime(Valid_from, '%Y-%m-%d') if Valid_from else None

            if Valid_to < Valid_from:\
                return redirect(url_for('staff_discount_detail.index2',discount_id=discount_id,errorMsg="Valid to should be bigger than Valid from!"))

        except ValueError:
            return redirect(url_for('staff_discount_detail.index2', discount_id=discount_id, details=details, errorMsg="Invalid date format!"))
        
        details.Valid_to = Valid_to
        details.Valid_from = Valid_from

    elif discount.Disc_type == 'Special Event':
        details = Special_event.query.filter_by(DID=discount_id).first()
        Valid_to = request.form.get('Valid_to')
        Valid_from = request.form.get('Valid_from')
        try:
            Valid_to = datetime.strptime(Valid_to, '%Y-%m-%d') if Valid_to else None
            Valid_from = datetime.strptime(Valid_from, '%Y-%m-%d') if Valid_from else None

            if Valid_to < Valid_from:\
                return redirect(url_for('staff_discount_detail.index2',discount_id=discount_id,errorMsg="Valid to should be bigger than Valid from!"))

        except ValueError:
            return redirect(url_for('staff_discount_detail.index2', discount_id=discount_id, details=details, errorMsg="Invalid date format!"))
        
        details.Valid_to = Valid_to
        details.Valid_from = Valid_from

    db.session.commit()

    return redirect(url_for('staff_discount_detail.index', discount_id=discount_id))

@staff_discount_detail.route('/staff/discount/delete/<int:discount_id>', methods=['POST'])
def delete(discount_id):
    discount = Discount.query.get(discount_id)
    print("msk delete")

    db.session.delete(discount)
    db.session.commit()

    if request.method == 'POST':
        return redirect(url_for('staff_discount.index'))