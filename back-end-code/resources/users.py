import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
                        # ^ this is a f that returns scrambled pwd
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user # this will be used to do the session


# make this a blueprint
users = Blueprint('users','users')

#test that my users route is working
@users.route('/', methods=['GET'])
def test_user_resource():
    return "user resource works for project"

@users.route('/register', methods=['POST'])
def register():
    payload = request.get_json()

    # since emails are case insensitive in the world
    payload['email'] = payload['email'].lower()
    # might as well do the same with the username
    payload['username'] = payload['username'].lower()
    print(payload)

    # see if the user exists
    try:
        models.User.get(models.User.email == payload['email'])
        models.User.get(models.User.username == payload['username'])

        return jsonify(
            data={},
            message=f"A user with the email or password already exists",
            status=401
        ), 401
    except models.DoesNotExist:
        # the user does not exist

        # scramble the password with bcrypt
        payload['password'] = generate_password_hash(payload['password'])

        created_user = models.User.create(
            **payload
        )

        print(created_user)

        login_user(created_user)

        # respond with a new a object and success message
        created_user_dict = model_to_dict(created_user)


        print(created_user_dict)

        print(type(created_user_dict['password']))
        created_user_dict.pop('password')

        return jsonify(
            data=created_user_dict,
            message=f"Successfully registered user {created_user_dict['email']}",
            status=201
        ), 201

@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()

    # look up the user by email
    try:
        user = models.User.get(models.User.email == payload['email'])

    # if we got here, we know a user with this email exists
        user_dict = model_to_dict(user)

        password_is_good = check_password_hash(user_dict['password'], payload['password'])

        # if the pw is good
        if (password_is_good):
            login_user(user, remember=True)


            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message=f"Successfully logged in {user_dict['email']}",
                status=200
            ), 200
        # else if pw is bad
        else:
            print('pw is no good')
            return jsonify(
                data={},
                message="Email or password is incorrect", # let's be vague
                status=401
            ), 401
            # respond -- bad username or password
    except models.DoesNotExist:
    # else if they don't exist
        print('username is no good')
        # respond -- bad username or password
        return jsonify(
            data={},
            message="Email or password is incorrect", # let's be vague
            status=401
        ), 401

@users.route('/logout', methods=["GET"])
def logout():
    logout_user() # this line will need to be imported
    return jsonify(
        data={},
        status=200,
        message= 'successful logout'
    ), 200
