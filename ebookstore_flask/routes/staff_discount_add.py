from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

staff_discount_add = Blueprint('staff_discount_add', __name__)

@staff_discount_add.route('/staff/discount/add', methods=['GET','POST'])
def index():
    from ebookstore_flask import db
    from ebookstore_flask.models.discount import Discount
    from ebookstore_flask.models.special_event import Special_event
    from ebookstore_flask.models.shipping import Shipping
    from ebookstore_flask.models.seasoning import Seasoning

    details = {'Valid_to': None, 'Valid_from': None, 'Min_purchase': None}
    Disc_name = request.form.get('Disc_name')
    Disc_code = request.form.get('Disc_code')
    Policy_desc = request.form.get('Policy_desc')
    Disc_type = request.form.get('Disc_type')
    Disc_value = request.form.get('Disc_value')
    Max_usage = request.form.get('Max_usage')
    # discount = {
    #     'Disc_name': request.form.get('Disc_name'),
    #     'Disc_code': request.form.get('Disc_code'),
    #     'Policy_desc': request.form.get('Policy_desc'),
    #     'Disc_type': request.form.get('Disc_type'),
    #     'Disc_value': request.form.get('Disc_value'),
    #     'Max_usage': request.form.get('Max_usage'),
    # }
    print("disc_code get",Disc_code)
    discount = {
            "Disc_name" : Disc_name,
            "Disc_code" : Disc_code,
            "Policy_desc" : Policy_desc,
            "Disc_type" : Disc_type,
            "Disc_value" : Disc_value,
            "Max_usage" : Max_usage 
        }

    if request.method == 'POST':
        #constraint
        if Discount.query.filter_by(Disc_code=Disc_code).first():
            print("render1")
            return render_template('/staff/discount_add.html', discount=discount, details=details, errorMsg="Discount Code already exists!")
        if '.' not in Disc_value: 
            print("render2")
            return render_template('/staff/discount_add.html', discount=discount, details=details, errorMsg="Discount Value should be decimal!")
        

        if Disc_type == 'Shipping':
            Min_purchase = request.form.get('Min_purchase')
            if Min_purchase.isdigit() == False:
                return render_template('/staff/discount_add.html', discount=discount, details=details, errorMsg="Minimal purchase should be number!")
            details['Min_purchase'] = Min_purchase
            new_to_spec = Shipping(Min_purchase=Min_purchase)
        elif Disc_type in ['Seasoning', 'Special Event']:
            Valid_to = request.form.get('Valid_to')
            Valid_from = request.form.get('Valid_from')
            try:
                details['Valid_to'] = datetime.strptime(Valid_to, '%Y-%m-%d') if Valid_to else None
                details['Valid_from'] = datetime.strptime(Valid_from, '%Y-%m-%d') if Valid_from else None

                if details['Valid_to'] < details['Valid_from']:
                    print("render3")
                    return render_template('/staff/discount_add.html', discount=discount, details=details, errorMsg="Valid to should be bigger than Valid from!")

            except ValueError:
                print("render4")
                return render_template('/staff/discount_add.html', discount=discount, details=details, errorMsg="Invalid date format!")

            if Disc_type == 'Seasoning':
                new_to_spec = Seasoning(Valid_to=details['Valid_to'], Valid_from=details['Valid_from'])
            else:
                new_to_spec = Special_event(Valid_to=details['Valid_to'], Valid_from=details['Valid_from'])

        new_discount = Discount(
            Disc_name=Disc_name,
            Disc_code=Disc_code,
            Policy_desc=Policy_desc,
            Disc_type=Disc_type,
            Disc_value=Disc_value,
            Max_usage=Max_usage
        )
        db.session.add(new_discount)
        db.session.commit()

        new_to_spec.DID = new_discount.DID
        db.session.add(new_to_spec)
        db.session.commit()

        print("render add_save")
        return render_template('/staff/discount_add_save.html', discount=new_discount, details=details, discount_ID=new_discount.DID)

    return render_template('/staff/discount_add.html', discount=discount, details=details)