from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name = "home"),
    path("profile", Profile.as_view(), name = "profile"),
    path("lock-screen", LockScreen.as_view(), name = "lock_screen"),
]
