def get_role(C_flag, S_flag, A_flag):
   if C_flag: return "Customer"
   elif S_flag: return "Staff"
   elif A_flag: return "Administrator"

def check_role(user, required_role=''):
   from ebookstore_flask.utils.session import check_session
   from flask import abort
   session_data = check_session()
   session_role = session_data[1]
   if session_role != user.Role: abort(403)
   if required_role and session_role != required_role: abort(403)
   return True