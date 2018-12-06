from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Perfil
from feed.models import Tweet

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/feed/list_tweets/')
        else:
           pass

    return render(request, 'users/login.html')

def view_profile(request, id):

    profile = Perfil.objects.get(id = id)
    list_tweets = Tweet.objects.filter(perfil_id = id)

    return render(
        request, 
        'users/profile.html', 
        {
            "profile" : profile,
            "list_tweets" : list_tweets
        }
    )