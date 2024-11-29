from flask import Blueprint, render_template, request, redirect, url_for, make_response
from models import db
from utils import session
login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def index():
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      query = db.session.execute('''
         SELECT *
         FROM MEMBER
         WHERE "Email" = :email;
      ''', {'email': email})
      user = query.fetchone()
      if user:
         if user[3]==password:
            session_id = session.add_session(user[5], user[0])
            resp = make_response(redirect(url_for('home.index')))
            resp.set_cookie('session_id', session_id, max_age=60*60*24)
            next_url = request.args.get('next')
            if next_url: return redirect(next_url)
            return resp
         else: return render_template("login.html", error="Invalid password")
      else: return render_template("login.html", error="User not found")
   return render_template("login.html",)