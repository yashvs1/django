from django.urls import path
from django.contrib import admin
 
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("about",views.about, name="about"),
    path("intro",views.intro,name="intro"),
    path("contact",views.Contact,name="contact")
]