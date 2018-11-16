from django.shortcuts import render
from django.http import HttpResponse


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
    return render(
        request,
        "feed.htm",
        {
            "feed":tweets
        }
    )