from django.shortcuts import render
from django.template import loader
from .forms import LoginForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def home(request):
    template = loader.get_template("wastagerecord/home.html")
    placeholder = {"text": "hello world"}
    context = {"placeholder": placeholder}
    return HttpResponse(template.render(context, request))


def login(request):
    form = LoginForm()
    return render(request, "wastagerecord/login.html", {"form": form})


def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/home/")
    else:
        form = LoginForm()
        return render(request, "login/", {"form": form})