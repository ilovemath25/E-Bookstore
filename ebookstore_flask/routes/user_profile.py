from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/user/profile')
def index():
   check_session()
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
   check_session()
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
   check_session()
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
   print(cards)
   credit_cards = [card[0] for card in cards]
   for i in range(len(credit_cards)):
      bin_info = bin_number_checker(credit_cards[i].Number[:6])
      credit_cards[i] = {
         'Number': credit_cards[i],
         'Card_type': bin_info.get('Card_type', 'Unknown'),
         'Bank': bin_info.get('Bank', 'Unknown')
      }
   return render_template('user/user_profile_credit_card.html', credit_cards=credit_cards)

@user_profile.route('/user/profile/change_password')
def change_password():
   return render_template('user/change_password.html')

@user_profile.route('/user/profile/order')
def order():
   return render_template('user/order.html')

@user_profile.route('/user/profile/discount')
def discount():
   return render_template('user/discount.html')