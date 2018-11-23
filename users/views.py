from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Perfil
from feed.models import Post

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(username)
            login(request, user)
            return redirect('/feed/hi')
        else:
           pass

    return render(request, 'login.html')

def view_profile(request, id):
    profile = Perfil.objects.get(id=id)
    
    tweets = Post.objects.filter(perfil_id = id)

    return render(
        request, 
        'users/profile.html', 
        {
            "id" : profile.id,
            "name" : profile.user.username,
            "tweets_arr" : tweets
        }
    )