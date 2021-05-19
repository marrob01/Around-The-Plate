
from flask import Flask, jsonify

import os #For my eviorn

import models

DEBUG=True # print nice helpful error msgs since im in development
PORT=8000

from flask_cors import CORS

from dotenv import load_dotenv

from flask_login import LoginManager

from resources.users import users

load_dotenv()

app = Flask(__name__) # instantiating the Flask class to create an app

app.secret_key = os.environ.get("FLASK_APP_SECRET")

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return  models.User.get(models.User.id == user_id)


CORS(users, origins=['http://localhost:3000'], supports_credentials=True) #for the users blueprint

app.register_blueprint(users, url_prefix='/api/v1/users') #register blueprint




if __name__ == '__main__':
    # when we start the app, set up out DB/tables as defined in models.property
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
