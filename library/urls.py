from django.urls import path
from library import views

urlpatterns = [
    path("", views.home, name="home"),
]