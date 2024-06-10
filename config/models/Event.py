from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, DateField, TextField, BooleanField
from config.database.database import db

class Event(Model):
    e_id = AutoField()
    name = CharField()
    description = TextField()
    start_date = DateField()
    end_date = DateField()
    location = CharField()
    credits_amount = IntegerField()
    organization = CharField()
    hours_amount = IntegerField()
    part_format = TextField()
    active = BooleanField()

    class Meta:
        database = db  # Использует базу данных, указанную в database.py