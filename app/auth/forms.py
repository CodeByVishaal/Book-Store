from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired(), Length(min=5, max=30, message='name must contain 5-30 characters')])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), 
        Length(8,20, message='password must contain  8-20 characters'),
        EqualTo('confirm')
        ])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), 
        EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Register")


