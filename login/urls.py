from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^join/$', views.join, name='join'),
    url(r'^$', views.login),
]
