from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("login/login_check/", views.login_check, name="login_check")
]
