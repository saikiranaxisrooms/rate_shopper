import json
from django.shortcuts import render
from rest_framework.views import APIView
from hotels.models import Hotel
from rest_framework.response import Response
from rest_framework import status
import requests
from auth.models import Authentication

# Create your views here.
class HotelList(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        hotelname = body.get('hotelname', '')
        country = body.get('country', '')
        city = body.get('city', '')
        state = body.get('state', '')
        zip_code = body.get('zip', '')
        keyword = body.get('keyword', '')
        pagenumber = body.get('pagenumber', 0)
        pagesize = body.get('pagesize', 0)
        geolocation = body.get('geolocation', {})
        latitude = geolocation.get('latitude', '')
        longitude = geolocation.get('longitude', '')
        radius = geolocation.get('radius', '')

        hotel_url = 'https://api.ratemetrics.com/hotels'
        payload = {
            "hotelname": hotelname,
            "country": country,
            "city": city,
            "state": state,
            "zip": zip_code,
            "keyword": keyword,
            "pagenumber": pagenumber,
            "pagesize": pagesize,
            "geolocation": {
                "latitude": latitude,
                "longitude": longitude,
                "radius": radius }}
        access_token = Authentication.objects.all()[0]['access_token']
        headers = {'Authorization': access_token}
        try:
            response = requests.post(hotel_url, json=payload, headers=headers)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                return Response(response.json(), status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

