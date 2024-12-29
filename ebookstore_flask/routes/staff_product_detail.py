from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.special_event import Special_event
from ebookstore_flask.models import db
from ebookstore_flask.utils.role import check_role
from datetime import datetime

staff_product_detail = Blueprint('staff_product_detail', __name__)

@staff_product_detail.route('/staff/product_detail/<int:product_id>')
def index(product_id):
    check_role("Staff", "Administrator")

    product = Product.query.filter_by(PID=product_id).first()

    return render_template(
        "staff/product_detail.html",
        product=product
    )
@staff_product_detail.route('/staff/product_detail/<int:product_id>/edit')
def index2(product_id):
    check_role("Staff", "Administrator")

    errorMsg = request.args.get('errorMsg', '')

    product = Product.query.filter_by(PID=product_id).first()

    return render_template(
        "/staff/product_detail_edit.html",
        product = product,
        errorMsg=errorMsg
    )
    

@staff_product_detail.route('/staff/product_detail/<int:product_id>/update', methods=['POST'])
def update_product(product_id):
    product = Product.query.filter_by(PID=product_id).first()

    Price = request.form.get('Product_price')
    Stock_quantity = request.form.get('Product_stock')

    #constraint    
    if Price.isdigit() == False: 
        return redirect(url_for('staff_product_detail.index2',product_id=product_id,errorMsg="Price should be number!"))
    if Stock_quantity.isdigit() == False: 
        return redirect(url_for('staff_product_detail.index2',product_id=product_id,errorMsg="Stock quantity should be number!"))
    
    product.Name = request.form.get('Product_name')
    product.Desc = request.form.get('Product_desc')
    product.Author = request.form.get('Product_author')
    product.Price = Price
    product.Stock_quantity = Stock_quantity
    product.Category = request.form.get('Product_categ')
    product.Product_pict = request.form.get('Product_pict')

    db.session.commit()

    return redirect(url_for('staff_product_detail.index', product_id=product_id))

@staff_product_detail.route('/staff/product/delete/<int:product_id>', methods=['POST'])
def delete(product_id):
    product = Product.query.get(product_id)

    db.session.delete(product)
    db.session.commit()

    if request.method == 'POST':
        return redirect(url_for('staff_product.index'))