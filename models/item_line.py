from . import db
from sqlalchemy import Enum

class Item_line(db.Model):
    __tablename__ = 'Item_line'
    
    LID = db.Column(db.Integer, primary_key=True, nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('Product.PID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    OID = db.Column(db.Integer, db.ForeignKey('Order.OID', onupdate="CASCADE", ondelete="SET NULL")) 
    SCID = db.Column(db.Integer, db.ForeignKey('ShoppingCart.SCID', onupdate="CASCADE", ondelete="SET NULL")) 
    Line_type = db.Column(Enum('Order', 'ShoppingCart', name='line_type_enum'), nullable=False) 
    Quantity = db.Column(db.Integer, nullable=False) 