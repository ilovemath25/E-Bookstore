from . import db

class Product(db.Model):
    __tablename__ = 'Product'
    
    PID = db.Column(db.Integer, primary_key=True, nullable=False)  
    SMID = db.Column(db.Integer, db.ForeignKey('Member.MID'), nullable=False)  
    SpEvent_ID = db.Column(db.Integer, db.ForeignKey('Special_event.DID'), nullable=True) 
    Name = db.Column(db.String(50), nullable=False)  
    Desc = db.Column(db.String(1000), nullable=True)  
    Author = db.Column(db.String(30), nullable=True)  
    Price = db.Column(db.Integer, nullable=False)  
    Stock_quantity = db.Column(db.Integer, nullable=False)  
    Category = db.Column(db.String(20), nullable=True) 
    Product_pict = db.Column(db.String(100), nullable=True) 
    Sale_count = db.Column(db.Integer, nullable=True)  
