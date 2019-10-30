from app import app
# from flask import render_template, flash, redirect,url_for
from flask import *
from app.app_login_form import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import request
from werkzeug.urls import url_parse
@app.route('/')
@app.route('/index')
@login_required
def index():
    return "MY first flask script says hello world"

@app.route('/p1')

def p1():
    user = {'username': 'brother'}
    messages=[
        {
              'sender':'human1',
              'message':'iam a human'


        },{
            'sender':'robot',
            'message':'iam a robot'


        }]
    
    return render_template('firstPage.html',title="first page", user=current_user,messages = messages)
@app.route('/login',methods=['POST']) # Login info should not be sent with GET request
def login():
    if current_user.is_authenticated:
        return redirect(url_for('p1'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
