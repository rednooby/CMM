from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views #login하기위해
from . import views


urlpatterns = [
    url(r'^join/$', views.join, name='join'),
    
    #https://github.com/django/django/blob/1.10.6/django/contrib/auth/views.py#L62
    #에 def login을 보면 기본 request받고 기본 디렉토리가 내가 설정한 것과 다르기 때문에 kwargs를 사용해 임의 지정 함
    url(r'^$', auth_views.login, name='login', kwargs={'template_name': 'login/login.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'login/login.html'}),
]
