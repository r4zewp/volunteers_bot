from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, BooleanField
from config.database.database import db

class User(Model):
    id = AutoField()
    username = CharField()
    phone_number = CharField()
    telegram_user_id = BigIntegerField()
    is_admin = BooleanField()

    class Meta:
        database = db  # Использует базу данных, указанную в database.py