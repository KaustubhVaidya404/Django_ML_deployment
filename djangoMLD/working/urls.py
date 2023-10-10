from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.Welcome),
    path('user', views.User)
]
