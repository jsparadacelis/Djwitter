from django.urls import include, path
from users.views import login_view, view_profile

urlpatterns = [
    path("", login_view , name="login_view"),
    path("profile/<int:id>", view_profile, name="profile")
]