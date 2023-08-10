from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("index/",views.index,name="index"),
]