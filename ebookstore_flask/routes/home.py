from flask import Blueprint, render_template
from ebookstore_flask.models.member import Member

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
def index():
   members = Member.query.all()
   return render_template("home.html", members=members)