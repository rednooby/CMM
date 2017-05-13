from django.conf.urls import url
from . import views

#/mypage/??
urlpatterns = [
    url(r'^$', views.managment, name='managment'),
]
