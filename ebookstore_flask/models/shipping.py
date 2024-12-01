from . import db

class Shipping(db.Model):
    __tablename__ = 'Shipping'
    DID = db.Column(db.Integer, db.ForeignKey('Discount.DID', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False)
    Min_purchase = db.Column(db.Integer)
