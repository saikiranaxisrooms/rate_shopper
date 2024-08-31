import json
from django.shortcuts import render
from rest_framework.views import APIView
from auth.models import Authentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests

# Create your views here.
class AuthToken(APIView):
    def get(self,request):
        auth_url = 'https://api.ratemetrics.com/authtoken'
        username = settings.AUTH_CONFIG['username']
        password = settings.AUTH_CONFIG['password']
        response = requests.post(auth_url, json={"username": username, "password": password})
        token_type = 'Bearer'
        access_token = token_type +' '+ json.loads(response.text)['access_token']
        start_time =  json.loads(response.text)['issued']
        end_time = json.loads(response.text)['expires']

        if Authentication.objects.filter(username=username):
            token_exists = Authentication.objects.filter(username=username)[0]
            token_exists.update(auth_url=auth_url, username=username, password=password, access_token=access_token,
                                start_time=start_time, end_time=end_time)
        else:
            Authentication(auth_url=auth_url, username=username, password=password, access_token=access_token,
                           start_time=start_time, end_time=end_time).save()
        return Response("success", status=status.HTTP_200_OK)


