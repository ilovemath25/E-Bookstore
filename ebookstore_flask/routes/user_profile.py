from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions
from ebookstore_flask.models.member import Member
from ebookstore_flask.models.credit_card import Credit_card
from ebookstore_flask.utils.credit_card import bin_number_checker

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/user/profile')
def index():
   if not check_session(): return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   return render_template(
      'user/user_profile.html',
      user=user,
      role=role
   )

@user_profile.route('/user/profile/edit', methods=['POST','GET'])
def edit():
   if not check_session(): return redirect(url_for('login.index'))
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   if not email: return redirect(url_for('login.index'))
   role = None
   session_data = check_session()
   if(session_data): _, role = session_data
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )

   return render_template(
      'user/user_profile_edit.html',
      user=user,
      role=role
   )

@user_profile.route('/user/profile/credit_card')
def credit_card():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
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
      credit_cards[i] = '**** **** **** ' + credit_cards[i][-4:]
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   return render_template(
      'user/user_profile_credit_card.html',
      credit_cards=credit_cards,
      role=session_data[1] if session_data else None
   )

@user_profile.route('/user/profile/credit_card/edit', methods=['POST', 'GET'])
def credit_card_edit():
   session_data = check_session()
   if not session_data:
      next_url = request.args.get('next')
      return redirect(next_url if next_url else url_for('home.index'))
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
      credit_cards[i] = '**** **** **** ' + credit_cards[i][-4:]
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Brand': bin_info.get('Brand', 'Unknown'),
         'Issuer': bin_info.get('Issuer', 'Unknown')
      }
   return render_template(
      'user/user_profile_credit_card_edit.html',
      credit_cards=credit_cards,
      role=session_data[1] if session_data else None
   )

@user_profile.route('/user/profile/change_password', methods=['GET', 'POST'])
def change_password():
    if not check_session():
        return redirect(url_for('login.index'))

    # Get user session
    session_id = request.cookies.get("session_id")
    sessions = load_sessions()
    email = sessions.get(session_id, [None])[0]
    if not email:
        return redirect(url_for('login.index'))

    # Fetch user from the database
    from ebookstore_flask.models.member import Member
    from ebookstore_flask.models import db

    user = Member.query.filter_by(Email=email).first()
    if not user:
        return "User not found.", 404

    if request.method == 'POST':
        old_password = request.form.get('currentPassword')
        new_password = request.form.get('newPassword')
        confirm_password = request.form.get('confirmNewPassword')
        print(user.Password , old_password)

        
        user.Password = new_password
        db.session.commit()

        return redirect(url_for('user_profile.index'))

    return render_template('user/user_profile_change_password.html', old_password=user.Password)

@user_profile.route('/user/profile/order')
def order():
   return render_template('user/order.html')

@user_profile.route('/user/profile/discount')
def discount():
   return render_template('user/discount.html')