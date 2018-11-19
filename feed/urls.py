from django.urls import include, path
from .views import hello_world
from feed.views import send_tweet

urlpatterns = [
    path("hi/", hello_world , name="hi"),
    path("send_tweet/", send_tweet , name="send_tweet")
]