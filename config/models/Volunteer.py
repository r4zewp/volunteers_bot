from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField
from database import db

class Volunteer(Model):
    v_id = AutoField()
    user_id = IntegerField()
    name = CharField()
    surename = CharField()
    middlename = CharField()
    education_typer = CharField()
    education_program = CharField()
    course_number = IntegerField()
    
    class Meta:
        database = db  # Использует базу данных, указанную в database.py