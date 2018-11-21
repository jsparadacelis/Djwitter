from django.urls import include, path
from users.views import login_view

urlpatterns = [
    path("login/", login_view , name="login")
]