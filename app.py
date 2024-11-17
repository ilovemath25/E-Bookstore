from flask import Flask, render_template
from models import db
from models.members import Members
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YourSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ilovemath25@localhost:5432/ebookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
   members = Members.query.all()
   return render_template("main.html", members=members)
if __name__=='__main__': app.run(debug=True, port=5000)
