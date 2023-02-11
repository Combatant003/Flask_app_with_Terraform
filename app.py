from flask import Flask,session
from flask_session import Session
from application.models import db
from os import urandom
from application.graphs import Draw_eng,Draw_chem,Draw_maths,Draw_phy
#---------------------------- Imports -----------------

app = None

def create_app():
    app = Flask(__name__,template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Student_DB.db'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    db.init_app(app)
    app.app_context().push()
    Draw_phy()
    Draw_maths()
    Draw_chem()
    Draw_eng()
    return app

app = create_app()

from application.views import *

if __name__ == '__main__':
    app.debug = True
    app.secret_key = urandom(24)
    app.run(threaded=True, host='0.0.0.0', port=5000)
