from app import db
from .discount import Discount

class Seasoning(db.Model):
    __tablename__ = 'seasoning'

    DID = db.Column(db.Integer, db.ForeignKey('discount.DID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True, nullable=False)
    Valid_to = db.Column(db.Date, nullable=False)
    Valid_from = db.Column(db.Date, nullable=False)

    __table_args__ = (
        db.CheckConstraint('Valid_to >= Valid_from', name='valid_date_range'),
    )
