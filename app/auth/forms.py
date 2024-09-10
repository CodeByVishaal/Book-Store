from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):

    name = StringField("What's your Name")
    email = StringField("What's your Email")
    submit = SubmitField("Register")

