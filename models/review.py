from . import db

class Review(db.Model):
    __tablename__ = 'Review'
    
    RID = db.Column(db.Integer, primary_key=True, nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('Product.PID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    MID = db.Column(db.Integer, db.ForeignKey('Member.MID', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    Time = db.Column(db.DateTime, nullable=False)
    Rate = db.Column(db.Integer, nullable=False)
    Rev_text = db.Column(db.String(500))
    Rev_picture = db.Column(db.String(255))
    Rev_video = db.Column(db.String(255)) 
    Reply_RID = db.Column(db.Integer, db.ForeignKey('Review.RID', onupdate="CASCADE", ondelete="SET NULL"))

#    def __repr__(self):
#        return f'<Review {self.RID}>'