from . import db
class Orders(db.Model):
   __tablename__ = 'Orders'
   OID = db.Column(db.Integer, primary_key=True, nullable=False)
   MID = db.Column(db.Integer, foreign_key=True, nullable=False)
   Credit_num = db.Column(db.String(16), foreign_key=True)
   Time = db.Column(db.Timestamp, nullable=False)
   Ship_address = db.Column(db.String(200), nullable=False)
   Ship_fee = db.Column(db.Integer, nullable=False)
   Status = db.Column(db.String(15), db.Enum('Received','Processing','Shipping','Closed'), nullable=False)
   Pay_method = db.Column(db.String(15), db.Enum('Credit card','COD'), nullable=False),
   Tot_price = db.Column(db.Integer)