from django.urls import path
from hotels import views

urlpatterns = [
    path('hotel_list', views.HotelList.as_view())
]