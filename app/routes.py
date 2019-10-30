from app import app,db
from flask import render_template, flash, redirect,url_for
from app.app_login_form import LoginForm,RegistrationForm
from flask_login import current_user,login_user,logout_user
from app.models import User
from flask_login import login_required



@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("firstPage.html", title='Home Page', posts=posts)

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
@app.route('/login',methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None :
            flash('Invalid username ')
            return redirect(url_for('login')) 
        if not user.check_password(form.password.data):
                flash('Invalid  password')
                return redirect(url_for('login')) 
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login_form.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
