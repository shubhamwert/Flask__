from flask import Flask
from configration import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
login=LoginManager(app)
migrate=Migrate(app,db)
db.create_all()
login.login_view = 'login'
                                                


from app import routes,models
