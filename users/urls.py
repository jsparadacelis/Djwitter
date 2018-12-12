from django.urls import include, path
from .views import login_view, view_profile, follow_profile

urlpatterns = [
    path("", login_view , name="login_view"),
    path("profile/<int:id>", view_profile, name="profile"),
    path("follow_profile/<int:id>", follow_profile, name="follow_profile")
]