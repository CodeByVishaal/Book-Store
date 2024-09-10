from flask import request, render_template, flash, redirect, url_for
from app.auth import authentication as at
from app.auth.forms import RegistrationForm
from app.auth.models import User

@at.route('/register', methods=['GET', 'POST'])

def register_user():
    
    name = None
    email = None
    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('User registered successfully!')
        return redirect(url_for('at.login_user'))

    return render_template('registration.html', form=form)

