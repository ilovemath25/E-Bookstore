from flask import Blueprint, render_template, request, redirect, url_for, make_response
from ebookstore_flask.utils.session import check_session
login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def index():
   if check_session():
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   if request.method == 'POST':
      from ebookstore_flask.models.member import Member
      from ebookstore_flask.utils.session import add_session, check_role
      email = request.form.get('email')
      password = request.form.get('password')
      user = (
         Member.query                     # SELECT * FROM "Member"
         .filter(Member.Email == email)   # WHERE "Email" = <email>;
         .all()
      )
      user = user[0]
      if user:
         if user.Password==password:
            role = check_role(user.C_flag, user.S_flag, user.A_flag)
            session_id = add_session(user.Email, user.MID, role)
            resp = make_response(redirect(url_for('home.index')))
            resp.set_cookie('session_id', session_id, max_age=60*60*24)
            next_url = request.args.get('next')
            if next_url: return redirect(next_url)
            return resp
         else: return render_template("/login/login.html", error="Invalid password")
      else: return render_template("/login/login.html", error="User not found")
   return render_template("/login/login.html",)