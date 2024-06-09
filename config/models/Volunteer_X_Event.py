from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, DateField, TextField, BooleanField
from database import db

class Event_X_Volunteer(Model):
    id = AutoField()
    event = ForeignKeyField(Event, backref='volunteers')
    volunteer = ForeignKeyField(Volunteer, backref='events')
    approved = BooleanField()
    appeared = BooleanField()
    hours_credited = IntegerField()
    
    @property
    def hours(self):
        return self.hours_credited / 8

    class Meta:
        database = db
        indexes = (
            (('event', 'volunteer'), True),
        )