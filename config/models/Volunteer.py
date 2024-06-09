from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, ForeignKeyField
from database import db
from models.User import User

class Volunteer(Model):
    v_id = AutoField()
    user = ForeignKeyField(User, backref='volunteers')
    name = CharField()
    surename = CharField()
    middlename = CharField()
    education_typer = CharField()
    education_program = CharField()
    course_number = IntegerField()
    email = CharField()
    
    class Meta:
        database = db  # Использует базу данных, указанную в database.py