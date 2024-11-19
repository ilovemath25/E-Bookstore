from . import db
class Discount(db.Model):
    __tablename__ = 'discount'
    DID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Disc_code = db.Column(db.String(20), unique=True, nullable=False)
    Disc_value = db.Column(db.Numeric, nullable=False)
    Disc_type = db.Column(db.Enum('Shipping', 'Seasonings', 'Special Events', name='Disc_type'), nullable=False)
    Disc_name = db.Column(db.String(50), nullable=False)
    Policy_desc = db.Column(db.String(1000), nullable=False)
    Disc_desc = db.Column(db.String(1000))
    Max_usage = db.Column(db.Integer)

    seasoning = db.relationship('Seasoning', backref='discount', uselist=False, cascade="all, delete-orphan")
    shipping = db.relationship('Shipping', backref='discount', uselist=False, cascade="all, delete-orphan")
