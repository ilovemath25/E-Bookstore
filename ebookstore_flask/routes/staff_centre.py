from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session
from ebookstore_flask.utils.role import check_role

staff_centre= Blueprint('staff_centre', __name__)

@staff_centre.route('/staff_centre')
def index():
   check_role("Staff", "Administrator")
   from ebookstore_flask.models.member import Member
   
   return render_template('staff/staff_centre.html')