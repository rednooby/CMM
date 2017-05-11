from django.conf.urls import url
from django.contrib.auth import views as auth_views #logout하기위해
from . import views
from django.conf import settings

#/index/??
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/', auth_views.logout, name='logout', 
    	kwargs={'next_page': settings.LOGIN_URL}),
]
