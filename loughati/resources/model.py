from flask_sqlalchemy import SQLAlchemy
import logging as lg
from . import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lougha:Lalo_gh1@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id_User = db.Column(db.Integer,primary_key = True)
    userName = db.Column(db.String(20),nullable = False)
    password = db.Column(db.String(100),nullable = False)
    FName = db.Column(db.String(100),nullable = False)
    LName = db.Column(db.String(100),nullable = False)
    Email = db.Column(db.String(100),nullable = False)

    def __init__(self, username, password,Fname,Lname,Email):
        self.userName = username
        self.password = password
        self.FName = Fname
        self.LName = Lname
        self.Email = Email

def initdb():
    db.drop_all()
    db.create_all()
    db.session.add(User('imad','jelato','imad','merzoug','im'))
    db.session.add(User('ddd','jelato','imad','merzoug','im'))
    db.session.commit()
    lg.warning("Data Base initialized!")    