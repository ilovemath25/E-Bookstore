from . import db
class Order_item_amount(db.Model):
   __tablename__ = 'Order_item_amount'
   AID = db.Column(db.Integer, primary_key=True, foreign_key=True, nullable=False)
   OID = db.Column(db.Integer, foreign_key=True, nullable=False)
