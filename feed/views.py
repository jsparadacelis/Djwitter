from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from users.models import Perfil


from django.shortcuts import render, redirect
from .forms import TweetForm

from django.views.generic.list import ListView

#Lista todo los tweets
class list_tweets(ListView):

    #Nombre de la plantilla para la vista
    template_name = "posts/feed.html"
    #Modelo del cual se van a extraer los datos
    model = Tweet
    #NOmbre que se le da al diccionario del contexto para mostrar los datos en la plantilla
    context_object_name = "list_tweets"


def send_tweet(request):
    
    print(request.user.perfil)
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["content"]
            tweet = Tweet(
                perfil = request.user.perfil, 
                texto = data
            )
            tweet.save()
            return redirect('list_tweets')

    else:
        form = TweetForm()

    return render(
        request,
        'feed.html',
        {
            'form': form
        }
    )