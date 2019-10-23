import os
import peewee
from peewee import *

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
database = peewee.SqliteDatabase(PATH("../../data.sqlite"))


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class user(BaseModel):
    name = CharField()
    login_name = CharField()
    password = CharField()
    role = CharField()
    create_time = IntegerField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'user'

user.create_table()