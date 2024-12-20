from flask import Blueprint, render_template

staff_discount_detail = Blueprint('staff_discount_detail', __name__)

@staff_discount_detail.route('/staff/discount_detail/<int:discount_id>')
def index(discount_id):
   from ebookstore_flask.models.discount import Discount
   from ebookstore_flask.models.special_event import Special_event
   from ebookstore_flask.models.shipping import Shipping
   from ebookstore_flask.models.seasoning import Seasoning

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
       details=details
    )


    