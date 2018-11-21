from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import Perfil


from django.shortcuts import render, redirect
from .forms import TweetForm

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
        "feed.html",
        {
            "feed":tweets
        }
    )



def send_tweet(request):
    #perfil de prueba
    perfil = request.user.perfil
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["content"]
            post = Post(perfil = perfil, texto = data)
            post.save()
            return redirect('/feed/hi')

    else:
        form = TweetForm()

    return render(
        request,
        'feed.html',
        {
            'form': form
        }
    )