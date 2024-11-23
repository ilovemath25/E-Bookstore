from . import db

class CreditCard(db.Model):
    __tablename__ = 'Credit_card'
    
    Number = db.Column(db.String(16), primary_key=True, nullable=False)
    CMID = db.Column(db.Integer, db.ForeignKey('Member.MID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    Expiry_date = db.Column(db.Date, nullable=False) 
    CVV = db.Column(db.String(3), nullable=False)  
