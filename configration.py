import os

basedir = os.path.abspath(os.path.dirname(".."))


class Config(object):
        SECRET_KEY="#11WASD$$#BGD" or os.environ.get('SECRET_KEY')
        SQLALCHEMYURL_DATABASE_URI=os.environ.get("DATABASE_URL") or \
                'sqlite:///'+os.path.join(basedir,'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False