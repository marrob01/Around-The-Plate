import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
                        # ^ this is a f that returns scrambled pwd
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user # this will be used to do the session


# make this a blueprint
users = Blueprint('users','users')


@users.route('/', methods=['GET'])
def test_user_resource():
    return "user resource works for project"
