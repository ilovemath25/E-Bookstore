def check_role(C_flag, S_flag, A_flag):
   if sum([C_flag, S_flag, A_flag]) > 1: raise ValueError("Error: Multiple roles selected")
   if C_flag: return "Customer"
   elif S_flag: return "Staff"
   elif A_flag: return "Administrator"