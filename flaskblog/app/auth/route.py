from flask import render_template, request, session, redirect, url_for
from forms import RegisterForm, LoginForm
from wtforms.validators import ValidationError
from models import User
from . import auth
from app import db, app
import traceback


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        if name is not None:
            session['username'] = name
            return redirect(url_for('index'))
    return render_template('auth/login.html')


@auth.route('/register', methods=['POST', 'GET'])
def register():
    reg_form = RegisterForm()
    name = reg_form.username.data
    password = reg_form.password.data
    email = reg_form.email.data
    if name is not None:
        user = User(username=name, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        session['username'] = name
        return redirect(url_for('index'))
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
