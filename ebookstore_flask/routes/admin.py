from flask import Blueprint, render_template, request, redirect, url_for, flash
from ebookstore_flask.utils.role import check_role
from ebookstore_flask.utils.session import load_sessions
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.order import Order
from ebookstore_flask import db
from datetime import datetime
from sqlalchemy import extract

admin = Blueprint('admin', __name__)

@admin.route('/admin/finance')
@admin.route('/admin/finance/<int:year>', methods=['GET','POST'])
def finance_overview(year = datetime.now().year):
    # Query orders to get financial data
    orders = Order.query.filter(extract('year', Order.Time) == year).all()
    
    total_revenue = sum(order.Tot_price for order in orders)
    total_expenses = sum(order.Tot_price * 0.7 for order in orders)  # Assuming 70% of total price is cost
    net_profit = total_revenue - total_expenses

    monthly_revenue = [0] * 12
    monthly_expenses = [0] * 12
    monthly_profit = [0] * 12
    monthly_sales = [0] * 12
    top_categories = [""] * 12

    for order in orders:
        month = order.Time.month - 1
        monthly_revenue[month] += order.Tot_price
        monthly_expenses[month] += order.Tot_price * 0.7
        monthly_profit[month] += (order.Tot_price - order.Tot_price * 0.7)
        monthly_sales[month] += 1

    for month in range(12):
        top_category = (
            db.session.query(Product.Category, db.func.count(Product.PID))
            .join(Order, Order.DID == Product.PID)
            .filter(db.extract('month', Order.Time) == month + 1)
            .group_by(Product.Category)
            .order_by(db.func.count(Product.PID).desc())
            .first()
        )
        top_categories[month] = top_category[0] if top_category else "N/A"

    total_revenue = "{:.2f}".format(total_revenue)
    total_expenses = "{:.2f}".format(total_expenses)
    net_profit = "{:.2f}".format(net_profit)

    role=check_role("Administrator")
    return render_template('admin/finance.html', 
        total_revenue=total_revenue, 
        total_expenses=total_expenses, 
        net_profit=net_profit,
        monthly_revenue=monthly_revenue,
        monthly_expenses=monthly_expenses,
        monthly_profit=monthly_profit,
        monthly_sales=monthly_sales,
        top_categories=top_categories,
        year_now=datetime.now().year,
        year=year,
        role=role
    )

@admin.route('/admin/user')
def manage_users():
    role=check_role("Administrator")
    users = Member.query.all()           # SELECT * FROM "Member"
    return render_template(
        'admin/admin_users.html',
        users=users,
        role=role
    )

@admin.route('/admin/user/<int:user_id>')
def manage_user_detail(user_id):
    role=check_role("Administrator")
    user = (
        Member.query                     # SELECT * FROM "Member"
        .filter(Member.MID == user_id)   # WHERE "MID" = <mid>;
        .first()
    )
    return render_template(
        'admin/admin_user_detail.html',
        user=user,
        role=role
    )

@admin.route('/admin/user/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    role=check_role("Administrator")
    user = (
        Member.query                     # SELECT * FROM "Member"
        .filter(Member.MID == user_id)   # WHERE "MID" = <mid>;
        .first()
    )
    if request.method == 'POST':
        user.F_name = request.form.get('F_name')
        user.L_name = request.form.get('L_name')
        user.Birth = request.form.get('Birth')
        user.Gender = request.form.get('Gender')
        user.Email = request.form.get('Email')
        user.Phone = request.form.get('Phone')
        user.Address = request.form.get('Address')
        db.session.commit()
        return redirect(url_for('admin.manage_users'))
    return render_template(
        'admin/admin_user_edit.html',
        user=user,
        role=role
    )
