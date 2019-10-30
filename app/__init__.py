from flask import Flask
from configration import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
<<<<<<< HEAD

=======
>>>>>>> 35395bed4c02ac261906fb60f73e4bf1a951ecc3


app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
login=LoginManager(app)
migrate=Migrate(app,db)
db.create_all()
<<<<<<< HEAD
login=LoginManager(app)
login.login_view = 'login'
=======
login.login_view = 'login'
                                                
>>>>>>> 35395bed4c02ac261906fb60f73e4bf1a951ecc3


from app import routes,models
