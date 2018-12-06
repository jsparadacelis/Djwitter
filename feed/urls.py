from django.urls import include, path
from .views import send_tweet,list_tweets

urlpatterns = [
    path("send_tweet/", send_tweet , name="send_tweet"),
    path("list_tweets/", list_tweets.as_view(), name="list_tweets")
]