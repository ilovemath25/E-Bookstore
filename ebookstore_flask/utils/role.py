def get_role(C_flag, S_flag, A_flag):
   if C_flag: return "Customer"
   elif S_flag: return "Staff"
   elif A_flag: return "Administrator"

def check_role(*required_role):
   from ebookstore_flask.utils.session import check_session
   from flask import abort
   if check_session():
      session_data = check_session()
      session_role = session_data[1]
      if len(required_role) and session_role not in required_role: abort(403)
      return session_role
   else:
      abort(403)
      return 0