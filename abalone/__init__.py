import os
import pickle
import traceback
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# BCrypt
bcrypt = Bcrypt(app)

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://15_legutko:A3p1z2h6j5@localhost/15_legutko'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Secret key
app.secret_key = 'C~\xb2\x95\x00:\xca\xc8b\x83\x89\xee\xf7)w&\xed\x96\xbe\x13\xfd\x88\x92\x81'

from abalone import views

# Load games
directory = os.fsencode('./games/')
try:
    for single_game in os.listdir(directory):
        filename = os.fsdecode(single_game)
        if filename.endswith('.p'):
            game_id = filename.split('.')[0]
            views.games[game_id] = pickle.load(open('games/' + filename, 'rb'))
except Exception as e:
    print(traceback.format_exc(e))
