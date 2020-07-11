from flask_wtf import FlaskForm
from wtforms import SubmitField


class ToolForm(FlaskForm):
    submit = SubmitField('Sign In')