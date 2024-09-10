from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

def email_exists(form, field):
    if User.query.filter_by(user_email = field.data).first():
        raise ValidationError('Email already exists')

class RegistrationForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired(), Length(5, 30, message='name must contain 5-30 characters')])
    email = StringField("E-mail", validators=[DataRequired(), Email(), email_exists])
    password = PasswordField("Password", validators=[DataRequired(), 
        Length(8,20, message='password must contain  8-20 characters'),
        EqualTo('confirm')
        ])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), 
        EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('Login')
