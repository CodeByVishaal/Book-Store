from flask import request, render_template
from app.auth import authentication as at
from app.auth.forms import RegistrationForm

@at.route('/register')
def register_user():
    form = RegistrationForm()
    return render_template('registration.html', form=form)

