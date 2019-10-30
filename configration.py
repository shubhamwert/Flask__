import os

basedir = os.path.abspath(os.path.dirname(".."))


class Config(object):
        SECRET_KEY="" or os.environ.get('SECRET_KEY') # Don't share secret key here. The Database can be exploited.
        SQLALCHEMYURL_DATABASE_URI=os.environ.get("DATABASE_URL") or \
                'sqlite:///'+os.path.join(basedir,'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
