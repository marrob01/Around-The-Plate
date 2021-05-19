from peewee import *
import datetime
from flask_login import UserMixin


DATABASE = SqliteDatabase('dogs.sqlite')


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
    likes = IntegerField()
    comments = TextField()

    class Meta:
        database = DATABASE

# class Favorites(Model):
#     favorite_section = ForeignKeyField(User, backref='favorite_recipe')
#     favorite = #the recipe model
#


    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES Created")
    DATABASE.close()
