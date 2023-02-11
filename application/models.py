from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    Student_id = db.Column(db.Integer,primary_key=True)
    Student_name = db.Column(db.String(100))
    Physics = db.Column(db.Integer)
    Maths = db.Column(db.Integer)
    Chemistry = db.Column(db.Integer)
    English = db.Column(db.Integer)

class Login(db.Model):
    Student_id = db.Column(db.Integer,primary_key=True)
    Password = db.Column(db.Integer, nullable=False)