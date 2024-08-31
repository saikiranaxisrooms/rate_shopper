from django.db import models
import json
import datetime
from mongoengine import *

# Create your models here.
class Hotel(Document):
    hotel_id = StringField()
    name = StringField()
    country = StringField()
    date_created = DateTimeField(default=datetime.datetime.now())
