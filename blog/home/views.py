from django.shortcuts import render
import datetime
# Create your views here.


def hai(request):
    return render(request, "index.html")


def define(request):
    return render(request, "login.html")