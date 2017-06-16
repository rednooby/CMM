from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views #login하기위해
from . import views


#/account/??
urlpatterns = [
    url(r'^index/my_view/(?P<id>.+)/$', views.my_list, name='my_list'),
    url(r'^index/view/(?P<id>.+)/$', views.my_view, name='my_view'),
    url(r'^index/edit/(?P<id>.+)/$', views.my_edit, name='my_edit'),
    url(r'^index/delete/(?P<id>.+)/$', views.my_delete, name='my_delete'),
    url(r'^join/$', views.join, name='join'),
    url(r'^index/$', views.index, name='index'),
    url(r'^mypage/$', views.Managment, name='Managment'),
    url(r'^mypage/PWC$', auth_views.password_change, name='password_change_done',
    	kwargs={'template_name': 'login/mypage.html'}),

    url(r'^mypage/(?P<act_name>.+)/$', views.account_info, name='account_info'),
    url(r'^mypage/(?P<act_name>.+)/edit/$', views.account_edit, name='account_edit'),
    url(r'^(?P<id>.+)/$', views.bankbook_new, name='bankbook_new'),
    #https://github.com/django/django/blob/1.10.6/ddjango/contrib/auth/views.py#L62
    #에 def login을 보면 기본 request받고 기본 디렉토리가 내가 설정한 것과 다르기 때문에 kwargs를 사용해 임의 지정 함
    url(r'^$', auth_views.login, name='login', 
    	kwargs={'template_name': 'login/login.html'}),
]
