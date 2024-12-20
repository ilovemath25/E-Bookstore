from flask import Blueprint, render_template, request, redirect, url_for, make_response
from models import db
login = Blueprint('login', __name__)

@login.route('/login_email', methods=['POST', 'GET'])
def index():
   if request.method == 'POST':
      from ebookstore_flask.models.member import Member
      from utils.session import add_session, check_role
      email = request.form.get('email')
      password = request.form.get('password')
      user = (
         Member.query                     # SELECT * FROM "Member"
         .filter(Member.Email == email)   # WHERE "Email" = <email>;
         .all()
      )
      if user:
         if user[3]==password:
            role = check_role(user[10], user[11], user[12])
            session_id = add_session(user[5], user[0], role)
            resp = make_response(redirect(url_for('home.index')))
            resp.set_cookie('session_id', session_id, max_age=60*60*24)
            next_url = request.args.get('next')
            if next_url: return redirect(next_url)
            return resp
         else: return render_template("/user/login.html", error="Invalid password")
      else: return render_template("/user/login.html", error="User not found")
   return render_template("/user/login.html",)