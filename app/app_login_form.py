from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
import wtforms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[wtforms.validators.DataRequired()])
    password = PasswordField('Password', validators=[wtforms.validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')