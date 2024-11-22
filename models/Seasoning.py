from . import db

class Seasoning(db.Model):
    __tablename__ = 'Seasoning'
    DID = db.Column(db.Integer, db.ForeignKey('Discount.DID', onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False)
    Valid_to = db.Column(db.Date, nullable=False)
    Valid_from = db.Column(db.Date, nullable=False)
    __table_args__ = (
        db.CheckConstraint('Valid_to >= Valid_from', name='valid_date_range'),
    )
    discount = db.relationship("Discount", back_populates="seasoning")
