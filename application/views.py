from flask import Flask, request
from flask import render_template, url_for, redirect, flash,session
from flask import current_app as app
from application.models import Login
from application.models import Student

@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pass']
        result = Login.query.filter(Login.Student_id == int(username), Login.Password== password).first()
        if result != None:
            stud_info = Student.query.filter(Student.Student_id == result.Student_id)
            name = stud_info.first()
            session["name"] = name.Student_name
            return redirect(url_for('profile',name=name.Student_name,id=name.Student_id))
        else:
            return render_template('login.html',error="Wrong Username or Password")
    return render_template('login.html')

@app.route('/profile/<name>/<id>',methods=["GET","POST"])
def profile(name,id):
    return render_template('profile.html',name=name,id=id)

@app.route('/report')
def generate_report():
    nam1 = session.get("name")
    stud_info = Student.query.filter(Student.Student_name == nam1)
    return render_template('report_card.html',name=nam1,sf=stud_info)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')