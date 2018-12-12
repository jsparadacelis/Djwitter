from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Perfil, Follow
from feed.models import Tweet
from django.http import HttpResponse

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

    profile = Perfil.objects.get(id=id)
    list_tweets = Tweet.objects.filter(perfil_id=id)
    list_followers = Follow.objects.filter(perfil = profile)


    return render(
        request, 
        'users/profile.html', 
        {
            "profile": profile,
            "list_tweets": list_tweets,
            "list_followers": list_followers
        }
    )

def follow_profile(request, id):

    profile_to_follow = Perfil.objects.get(id=id)
    new_follower = Follow.objects.create(
        perfil = profile_to_follow,
        seguidor = request.user.perfil
    )
   
    print(profile_to_follow.user.username)

    return redirect('/profile/'+str(id))
