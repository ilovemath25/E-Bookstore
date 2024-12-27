from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session

user_profile = Blueprint('user_profile', __name__)

@user_profile.route('/user/profile')
def index():
   if not check_session():
      next_url = request.url
      return redirect(url_for('login.index', next=next_url))
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
      next_url = request.url
      return redirect(url_for('login.index', next=next_url))
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

@user_profile.route('/user/logout', methods=['POST', 'GET'])
def logout():
   session_id = request.cookies.get("session_id")
   if session_id: delete_session(session_id) 
   response = redirect(url_for('home.index'))
   response.delete_cookie('session_id')
   return response
