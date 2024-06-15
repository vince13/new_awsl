from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")



def about(request):
    return render(request, "core/about.html")


def blog(request):
    return render(request, "core/blog.html")

def signup(request):
    return render(request, "core/register.html")


def login(request):
    return render(request, "core/login.html")

def services(request):
    return render(request, "core/services.html")