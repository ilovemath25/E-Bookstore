from . import db

class shoppingCart_item(db.Model):
    __tablename__ = 'ShoppingCart_item'

    SCID = db.Column(db.Integer, primary_key = True, nullable = False)
    CMID = db.Column(db.Integer, db.ForeignKey('Member.MID'))
    Tot_price = db.Column(db.Integer, nullable = False)