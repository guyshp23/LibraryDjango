from django.urls import path
from library import views

# Need to add the app name

urlpatterns = [
    path("", views.home, name="home"),
]