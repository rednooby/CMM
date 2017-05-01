from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login),
#    url(r'^join/', views.join_new),
]
