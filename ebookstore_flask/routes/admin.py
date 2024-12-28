from flask import Blueprint, render_template, request, redirect, url_for, flash
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.product import Product
from ebookstore_flask.models.order import Order
from ebookstore_flask import db

admin = Blueprint('admin', __name__)

# Manage Users
@admin.route('/admin/users')
def manage_users():
    users = Member.query.all()
    return render_template('admin/users.html', users=users)

@admin.route('/admin/users/<int:user_id>')
def view_user(user_id):
    user = Member.query.get_or_404(user_id)
    return render_template('admin/user_detail.html', user=user)

@admin.route('/admin/users/<int:user_id>/modify', methods=['GET', 'POST'])
def modify_user(user_id):
    user = Member.query.get_or_404(user_id)
    if request.method == 'POST':
        user.Name = request.form['name']
        user.Email = request.form['email']
        user.Status = request.form.get('status', user.Status)  # Example field
        db.session.commit()
        flash('User details updated successfully.', 'success')
        return redirect(url_for('admin.view_user', user_id=user_id))
    return render_template('admin/modify_user.html', user=user)

