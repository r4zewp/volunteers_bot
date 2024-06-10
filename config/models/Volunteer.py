from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, ForeignKeyField
from config.database.database import db
from config.models.User import User

class Volunteer(Model):
    v_id = AutoField()
    user = ForeignKeyField(User, backref='volunteers')
    name = CharField()
    surname = CharField()
    middlename = CharField()
    education_type = CharField()
    education_program = CharField()
    course_number = IntegerField()
    email = CharField()
    
    class Meta:
        database = db  # Использует базу данных, указанную в database.py