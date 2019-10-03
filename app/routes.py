from app import app
from flask import render_template
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
