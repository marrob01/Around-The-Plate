
import models


from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

#import current user
from flask_login import current_user, login_required


# creating our blueprint
# first arguments is the blueprint's name
# second arg is its import_name
recipes = Blueprint('recipes', 'recipes')

@recipes.route('/user_recipe', methods=['GET'])
def user_recipes_index():
    # return "route works"

    if current_user.is_authenticated:
        # or use a list comprehension
        recipe_dicts = [model_to_dict(recipe) for recipe in current_user.user_recipe]

        # print(dog_dicts)

        return jsonify({
            'data': recipe_dicts,
            'message': f"Successfully found {len(recipe_dicts)} recipes",
            'status': 200
        }), 200
    else:
        recipe_dicts = [model_to_dict(recipe) for dog in models.Recipe.select()]

        # print(recipe_dicts)

        return jsonify({
            'data': recipe_dicts,
            'message': f"Successfully found {len(recipe_dicts)} recipes",
            'status': 200
        }), 200

@recipes.route('/all_recipes', methods=['GET'])
def all_recipes_index():

    recipe_dicts = [model_to_dict(recipe) for recipe in models.Recipe.select()]

    # print(dog_dicts)

    return jsonify({
        'data': recipe_dicts,
        'message': f"Successfully found {len(recipe_dicts)} dogs",
        'status': 200
    }), 200


@recipes.route('/', methods=['POST'])
def create_recipe():
    # .get_json() attached to request will extract JSON from the request body
    pay = request.get_json() # this is like req.body in express
    print(current_user)
    print("-------------")

     # you should see request body in your terminal :)
    new_recipe = models.Recipe.create(name=pay['name'], recipe_name=pay['recipe_name'],steps=pay['steps'], likes=pay['likes'], comments=pay['comments'])
    print(new_recipe)

    recipe_dict = model_to_dict(new_recipe)

    return jsonify(
        data=recipe_dict,
        message='Successfully created dog!',
        status=201
    ), 201

# Complete like route
@recipes.route('/<id>/like', methods=['POST'])
def add_like(id):

    recipeToLike =  model_to_dict(models.Recipe.get_by_id(id))
    recipeToLikeO =  models.Recipe.get_by_id(id)

    print(recipeToLike)
    query = models.Recipe.update(likes=(models.Recipe.likes + 1)).where(models.Recipe.id ==id)

    query.execute() # Execute the query, returning number of rows updated.
    return jsonify(

        status= 200,
        message="Success on the like"
    ), 200


@recipes.route('/<id>', methods=["GET"])
def get_one_recipe(id):
    recipe = models.Recipe.get_by_id(id)
    return jsonify(
        data=model_to_dict(recipe),
        status= 200,
        message="Success"
    ), 200


@recipes.route('/<id>', methods=["PUT"])
def update_recipe(id):
    payload = request.get_json()
    models.Recipe.update(**payload).where(models.Recipe.id==id).execute()
    return jsonify(
        data=model_to_dict(models.Recipe.get_by_id(id)),
        status=200,
        message= 'resource updated successfully'
    ), 200

@recipes.route('/<id>', methods=["Delete"])
def delete_recipe(id):
    query = models.Recipe.delete().where(models.Recipe.id==id)
    query.execute()
    return jsonify(
        data='resource successfully deleted',
        message= 'resource deleted successfully',
        status=200
    ), 200
