
from flask import Flask, jsonify, after_this_request

import os #For my eviorn

import models

DEBUG=True # print nice helpful error msgs since im in development
PORT=8000

from flask_cors import CORS

from dotenv import load_dotenv

from flask_login import LoginManager

from resources.users import users
from resources.recipes import recipes

load_dotenv()

app = Flask(__name__) # instantiating the Flask class to create an app


app.secret_key = os.environ.get("FLASK_APP_SECRET")

from resources.users import users

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return  models.User.get(models.User.id == user_id)


CORS(users, origins=['http://localhost:3000', 'https://around-the-plate.herokuapp.com'], supports_credentials=True) #for the users blueprint
CORS(recipes, origins=['http://localhost:3000', 'https://around-the-plate.herokuapp.com'], supports_credentials=True)


app.register_blueprint(users, url_prefix='/api/v1/users') #register blueprint
app.register_blueprint(recipes, url_prefix='/api/v1/recipes') #register blueprint

# we don't want to hog up the SQL connection pool
# so we should connect to the DB before every request
# and close the db connection after every request

@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)


if __name__ == '__main__':
    # when we start the app, set up out DB/tables as defined in models.property
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()
