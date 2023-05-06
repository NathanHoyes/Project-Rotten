from django.shortcuts import render
from django.template import loader
from .forms import LoginForm
from django.http import HttpResponse


def index(request):
    template = loader.get_template("wastagerecord/home_page.html")
    placeholder = {"text": "hello world"}
    context = {"placeholder": placeholder}
    return HttpResponse(template.render(context, request))


def login(request):
    form = LoginForm()
    return render(request, "wastagerecord/login.html", {"form": form})