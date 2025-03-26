from django.urls import path
from . import views

urlpatterns = [
    path("", views.unipage, name="unipage"),
    path("landing", views.land, name="landing"),
]