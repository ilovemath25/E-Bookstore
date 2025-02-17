from . import db

class Discount(db.Model):
    __tablename__ = 'Discount'
    DID = db.Column(db.Integer, primary_key=True, nullable=False)
    Disc_code = db.Column(db.String(20), unique=True, nullable=False)
    Disc_value = db.Column(db.Numeric, nullable=False)
    Disc_type = db.Column(db.Enum('Shipping', 'Seasoning', 'Special Event'), nullable=False)
    Disc_name = db.Column(db.String(50), nullable=False)
    Policy_desc = db.Column(db.String(1000), nullable=False)
    Max_usage = db.Column(db.Integer)
