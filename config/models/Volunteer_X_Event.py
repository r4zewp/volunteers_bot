from peewee import Model, CharField, IntegerField, AutoField, BigIntegerField, DateField, TextField, BooleanField, ForeignKeyField
from config.database.database import db
from config.models.Event import Event
from config.models.Volunteer import Volunteer

class Volunteer_X_Event(Model):
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