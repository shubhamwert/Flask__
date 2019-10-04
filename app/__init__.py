from flask import Flask
from configration import Config
app = Flask(__name__)
app.config.from_object(Config)
from app import routes
