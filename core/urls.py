from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("services/", views.services, name="services"),
]

