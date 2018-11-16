from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
tweets = [
    {
        "user":"neftali",
        "text":"Mi tweet"
    },
    {
        "user":"mcguegi",
        "text":"My tweet"
    }
]

def hello_world(request):
    tweets = Post.objects.all()
    print(tweets)
    return render(
        request,
        "feed.htm",
        {
            "feed":tweets
        }
    )