from django.db import models
import datetime
from mongoengine import *
from rest_framework.views import APIView

# Create your models here.
class Authentication(Document):
    auth_url = StringField()
    username = StringField()
    password = StringField()
    access_token = StringField()
    start_time = StringField()
    end_time = StringField()