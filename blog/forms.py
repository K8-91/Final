from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    body = TextAreaField("body", validators=[DataRequired()])
    is_published = BooleanField("Published?")

