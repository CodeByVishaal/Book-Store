from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from app.auth.models import User

class EditForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateForm(FlaskForm):
    title = StringField('Title',  validators=[DataRequired()])
    author = StringField('Author',  validators=[DataRequired()])
    avg_rating = StringField('Rating', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    img_url = StringField('Image',  validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    pub_id = IntegerField('Publisher ID', validators=[DataRequired()])
    submit = SubmitField('Create Book')

