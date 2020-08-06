from app.home import bp
from flask import render_template


@bp.route("/")
def home():
    return render_template('home/home.html')
