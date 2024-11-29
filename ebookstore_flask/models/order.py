from . import db
class Order(db.Model):
   __tablename__ = 'Order'
   OID = db.Column(db.Integer, primary_key=True, nullable=False)
   CMID = db.Column(db.Integer, db.ForeignKey('Member.MID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
   SMID = db.Column(db.Integer, db.ForeignKey('Member.MID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
   Credit_num = db.Column(db.String(16), db.ForeignKey('Credit_card.Number', onupdate="CASCADE", ondelete="CASCADE"))
   Time = db.Column(db.DateTime, nullable=False)
   Ship_address = db.Column(db.String(200), nullable=False)
   Ship_fee = db.Column(db.Integer, nullable=False)
   Status = db.Column(db.String(15), db.Enum('Received','Processing','Shipping','Closed'), nullable=False)
   Pay_method = db.Column(db.String(15), db.Enum('Credit card','COD'), nullable=False)
   Tot_price = db.Column(db.Integer)