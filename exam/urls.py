from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from exam import views

urlpatterns = [
    path('',views.index,name="index"),
    url(r'^check/$',views.check,name="check"),
]
