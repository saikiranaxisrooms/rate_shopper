from django.urls import path
from . import views

urlpatterns = [
    path('auth_token', views.AuthToken.as_view())
]