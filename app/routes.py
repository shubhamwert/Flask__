from app import app
from flask import render_template
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
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login_form.html', title='Sign In', form=form)