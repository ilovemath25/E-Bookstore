from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash
from ebookstore_flask.utils.session import check_session, delete_session
from ebookstore_flask.models import db
from ebookstore_flask.models.member import Member
from datetime import date, datetime

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST', 'GET'])
def index():
   if check_session():
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   if request.method == 'POST':
      from ebookstore_flask.models.member import Member
      from ebookstore_flask.utils.session import add_session
      from ebookstore_flask.utils.role import get_role
      email = request.form.get('email')
      password = request.form.get('password')
      user = (
         Member.query                     # SELECT * FROM "Member"
         .filter(Member.Email == email)   # WHERE "Email" = <email>;
         .first()
      )
      if user:
         if user.Password==password:
            role = get_role(user.C_flag, user.S_flag, user.A_flag)
            session_id = add_session(user.Email, user.MID, role)
            resp = make_response(redirect(url_for('home.index')))
            resp.set_cookie('session_id', session_id, max_age=60*60*24)
            next_url = request.args.get('next')
            if next_url: return redirect(next_url)
            return resp
         else: return render_template("/login/login.html", error="Invalid password")
      else: return render_template("/login/login.html", error="User not found")
   return render_template("/login/login.html",)

@login.route('/user/logout', methods=['POST', 'GET'])
def logout():
   session_id = request.cookies.get("session_id")
   if session_id: delete_session(session_id) 
   response = redirect(url_for('home.index'))
   response.delete_cookie('session_id')
   return response

@login.route('/register', methods=['POST', 'GET'])
def register():
   if check_session():
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   
       # Get email from the form
   if request.method == 'POST':
      
      email = request.form.get('email')

      # Check if the email already exists
      existing_member = Member.query.filter_by(Email=email).first()

      if existing_member:
         # Email already registered
         flash("Email is already registered. Please use a different email.")
         return redirect(url_for('login.register'))  # Redirect back to the registration form

      elif not existing_member:
         first_name = request.form.get('firstName')
         last_name = request.form.get('lastName')
         email = request.form.get('email')
         gender = request.form.get('gender')
         phone_number = request.form.get('phoneNumber')
         password = request.form.get('password')
         confirm_password = request.form.get('confirmPassword')
         address = request.form.get('address')
         birth_date = request.form.get('birthDate')
         new_member = Member(
            F_name=first_name,
            L_name=last_name if last_name else None,
            Email=email.lower(),
            Gender=gender,
            Phone=phone_number,
            Password=password,  # Consider hashing the password
            Address=address if address else None,
            Birth=datetime.strptime(birth_date, '%Y/%m/%d').date() if birth_date else None,
            Reg_date=date.today(),
            A_flag=False,  # Example activation flag
            S_flag=False,  # Example subscription flag
            C_flag=True  # Example consent flag
            )

         try:
               # Add the new member to the database
               db.session.add(new_member)
               db.session.commit()
               return redirect(url_for('login.index'))  # Redirect to login page after successful registration
         except Exception as e:
               # Rollback in case of an error
               db.session.rollback()
               flash("An error occurred while registering. Please try again.")
               return redirect(url_for('login.register'))

   return render_template("/login/register.html",)