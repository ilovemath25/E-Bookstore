from . import db
class Members(db.Model):
   __tablename__ = 'Members'
   MID = db.Column(db.Integer, primary_key=True, nullable=False)
   F_name = db.Column(db.String(15), nullable=False)
   L_name = db.Column(db.String(15))
   Password = db.Column(db.String(15), nullable=False)
   Gender = db.Column(db.String(10), db.Enum('male', 'female', 'other'))
   Email = db.Column(db.String(100), unique=True, nullable=False)
   Phone = db.Column(db.Char)
   Birth = db.Column(db.Date)
   Address = db.Column(db.String(200))
   Reg_date = db.Column(db.Date, nullable=False)
   A_flag = db.Column(db.Boolean, nullable=False)
   S_flag = db.Column(db.Boolean, nullable=False)
   C_flag = db.Column(db.Boolean, nullable=False)
