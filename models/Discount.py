from . import db

class Discount(db.Model):
    __tablename__ = 'Discount'
    DID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    OID = db.Column(db.Integer, db.ForeignKey('Order.OID', onupdate="CASCADE", ondelete="CASCADE"))
    Disc_code = db.Column(db.String(20), unique=True, nullable=False)
    Disc_value = db.Column(db.Numeric, nullable=False)
    Disc_type = db.Column(db.ENUM('Shipping', 'Seasonings', 'Special Events', name='Disc_type'), nullable=False)
    Disc_name = db.Column(db.String(50), nullable=False)
    Policy_desc = db.Column(db.String(1000), nullable=False)
    Max_usage = db.Column(db.Integer)
    seasoning = db.relationship("Seasoning", back_populates="discount", uselist=False)
    shipping = db.relationship("Shipping", back_populates="discount", uselist=False)
