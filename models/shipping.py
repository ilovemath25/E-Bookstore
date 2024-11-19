from . import db
from .discount import Discount

class Shipping(db.Model):
    __tablename__ = 'shipping'

    DID = db.Column(db.Integer, db.ForeignKey('discount.DID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False)
    Min_Purchase = db.Column(db.Integer)
