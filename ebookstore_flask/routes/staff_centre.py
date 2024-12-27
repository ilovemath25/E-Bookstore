from flask import Blueprint, render_template, request, redirect, url_for
from ebookstore_flask.utils.session import check_session, load_sessions, delete_session

staff_centre= Blueprint('staff_centre', __name__)

@staff_centre.route('/staff_centre')
def index():
   if not check_session():
      next_url = request.url
      return redirect(url_for('login.index', next=next_url))
   from ebookstore_flask.models.member import Member
   
   session_id = request.cookies.get("session_id")
   sessions = load_sessions()
   email = sessions.get(session_id, [None])[0]
   role = sessions.get(session_id, [None])[1]
   if not email: return redirect(url_for('login.index'))
   if role == 'Customer': return redirect(url_for('home.index'))
   user = (
      Member.query                     # SELECT * FROM "Member"
      .filter(Member.Email == email)   # WHERE "Email" = <email>;
      .first()
   )
   return render_template('staff/staff_centre.html', user=user)