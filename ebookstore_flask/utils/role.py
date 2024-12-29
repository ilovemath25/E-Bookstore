def get_role(C_flag, S_flag, A_flag):
   if C_flag: return "Customer"
   elif S_flag: return "Staff"
   elif A_flag: return "Administrator"

def check_role(*required_role):
   from ebookstore_flask.utils.session import check_session
   from flask import abort
   session_data = check_session()
   session_role = session_data[1]
   for role in required_role:
      if role and session_role == "Customer": abort(403)
   return True