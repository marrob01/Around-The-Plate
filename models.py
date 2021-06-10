from peewee import *
import datetime
from flask_login import UserMixin
import os
from playhouse.db_url import connect


DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///recipes.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE


class Recipe(Model):
    name = ForeignKeyField(User, backref='user_recipe')
    created_date = DateTimeField(default=datetime.datetime.now)
    recipe_name = CharField()
    steps = TextField()
    likes = IntegerField(default=0)
    comments = TextField()

    class Meta:
        database = DATABASE

# MAke another model for user comments
# Make a model for favorite recipes

# Set up front end with react router basic nav bar for recipe routes
#think about layout and redo the wireframe


# class Favorites(Model):
#     favorite_section = ForeignKeyField(User, backref='favorite_recipe')
#     favorite = #the recipe model






def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe], safe=True)
    print("TABLES Created")
    DATABASE.close()
