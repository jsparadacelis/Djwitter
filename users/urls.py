from django.urls import include, path
from users.views import login_view, view_profile

urlpatterns = [
    path("login/", login_view , name="login"),
    path("profile/<int:id>", view_profile, name="profile")
]