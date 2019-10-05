from app import app
from flask import render_template, flash, redirect,url_for
from app.app_login_form import LoginForm
@app.route('/')
@app.route('/index')
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
    
    return render_template('firstPage.html',title="first page", user=user,messages = messages)
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('p1'))
    return render_template('login_form.html', title='Sign In', form=form)