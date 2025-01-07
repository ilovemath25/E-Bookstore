from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models import db
from ebookstore_flask.utils.role import check_role
from datetime import datetime

staff_product_add = Blueprint('/staff_product_add', __name__)

@staff_product_add.route('/staff/product/add', methods=['GET','POST'])
def add():
    session_data = check_session()
    role=check_role("Staff", "Administrator")
    email = session_data[0]
    member = Member.query.filter_by(Email=email).first()

    staff_ID = member.MID

    Pict =request.form.get('Product_pict')
    Name = request.form.get('Product_name')
    Desc = request.form.get('Product_desc')
    Author = request.form.get('Product_author')
    Price = request.form.get('Product_price')
    Stock_quantity = request.form.get('Product_stock')
    Category = request.form.get('Product_categ')
    SpEvent = request.form.get('Product_spEvent')

    product = {
        "Product_pict" : Pict,
        "Name" : Name,
        "Desc" : Desc,
        "Author" : Author,
        "Price" : Price,
        "Stock_quantity" : Stock_quantity,
        "Category" : Category,
        "SpEvent" : SpEvent
    }

    if request.method == 'POST':
        #constraint
        special_event = Special_event.query.filter_by(DID=SpEvent)
        if (not special_event) and (SpEvent!=''):
            return render_template('/staff/product_add.html',product=product, errorMsg="Special Event ID does not exist!")
        if Price.isdigit() == False: 
            return render_template('/staff/product_add.html',product=product, errorMsg="Price should be number!")
        if Stock_quantity.isdigit() == False: 
            return render_template('/staff/product_add.html',product=product, errorMsg="Stock quantity should be number!")
        if SpEvent == '':
            SpEvent = None
        
        new_product = Product(
            SMID = staff_ID,
            SpEvent_ID = SpEvent,
            Name = Name,
            Desc = Desc,
            Author = Author,
            Price = int(Price),
            Stock_quantity = int(Stock_quantity),
            Category = Category,
            Product_pict = Pict,
            Sale_count = 0
        )

        db.session.add(new_product)
        db.session.commit()

        return render_template('/staff/product_detail.html', product=new_product)
    
    return render_template('/staff/product_add.html',product=product, role=role)