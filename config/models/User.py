from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField
from config.database.database import db

class User(Model):
    id = AutoField()
    username = CharField()
    phone_number = CharField()
    telegram_id = BigIntegerField()

    class Meta:
        database = db  # Использует базу данных, указанную в database.py