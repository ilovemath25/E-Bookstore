from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/user/profile')
def index():
   if not check_session():
      return redirect(url_for('login.index'))
   from ebookstore_flask.models.member import Member
   
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   return render_template(
      'user/user_profile.html',
      user=user
   )

@user_profile.route('/user/profile/edit')
def edit():
   if not check_session():
      return redirect(url_for('login.index'))
   from ebookstore_flask.models.member import Member
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )

   return render_template(
      'user/user_profile_edit.html',
      user=user
   )

@user_profile.route('/user/profile/credit_card')
def credit_card():
   if not check_session():
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
   from ebookstore_flask.models.member import Member
   from ebookstore_flask.models.credit_card import Credit_card
   from ebookstore_flask.utils.credit_card import bin_number_checker
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   cards = (
      Credit_card.query.with_entities(Credit_card.Number) # SELECT "Credit_card"."Number" FROM "Credit_card"
      .join(Member, Member.MID == Credit_card.CMID)       # JOIN "Member" ON "Member"."MID" = "Credit_card"."CMID"
      .filter(Member.Email == email)                      # WHERE "Member"."Email" = <email>;
      .all()
   )
   credit_cards = [card[0] for card in cards]
   for i in range(len(credit_cards)):
      bin_info = bin_number_checker(credit_cards[i][:6])
      print(credit_cards[i][:6], bin_info)
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   return render_template('user/user_profile_credit_card.html', credit_cards=credit_cards)

@user_profile.route('/user/profile/change_password')
def change_password():
   if not check_session():
      return redirect(url_for('login.index'))
   from ebookstore_flask.models.member import Member
   from . import db
   
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   if request.method == 'POST':
      from werkzeug.security import check_password_hash, generate_password_hash
      from ebookstore_flask.models.member import Member

      user = Member.query.filter_by(Email=email).first()
      old_password = request.form['old_password']
      new_password = request.form['new_password']
      confirm_password = request.form['confirm_password']

      if not check_password_hash(user.Password, old_password):
         return "Old password is incorrect.", 400

      if new_password != confirm_password:
         return "Passwords do not match.", 400

      user.Password = generate_password_hash(new_password, method='sha256')
      db.session.commit()
      return redirect(url_for('user_profile.index'))
   return render_template('user/user_profile_change_password.html')

@user_profile.route('/user/profile/order')
def order():
   return render_template('user/order.html')

@user_profile.route('/user/profile/discount')
def discount():
   return render_template('user/discount.html')