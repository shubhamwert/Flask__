from app import db
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    db.create_all()
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 
    def set_Password(self,password):
        self.password_hash=generate_password_hash(password)
    def check_Password(self,password):
        return check_password_hash(password,self.password_hash)


class Post(db.Model):
    db.create_all()

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default="")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)