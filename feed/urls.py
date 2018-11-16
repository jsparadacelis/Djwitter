from django.urls import include, path
from .views import hello_world

urlpatterns = [
    path("hi/", hello_world , name="")
]