from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views #login하기위해
from . import views
from .views import *


urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^board/list/$', views.board_list, name='board_list'),
    url(r'^board/write/$', views.board_write, name='board_write'),
    url(r'^board/view/(?P<id>.+)/$', views.board_view, name='board_view'),
    url(r'^board/edit/(?P<id>.+)/$', views.board_edit, name='board_edit'),
    url(r'^board/delete/(?P<id>.+)/$', views.board_delete, name='board_delete'),
    
    url(r'^mypage/edit/(?P<id>.+)/$', views.account_edit, name='account_edit'),
    url(r'^mypage/delete/(?P<id>.+)/$', views.account_delete, name='account_delete'),
    
    url(r'^index/my_list/(?P<id>.+)/$', views.my_list, name='my_list'),
    url(r'^index/my_view/(?P<id>.+)/$', views.my_view, name='my_view'),
    url(r'^index/my_edit/(?P<id>.+)/$', views.my_edit, name='my_edit'),
    url(r'^index/my_delete/(?P<id>.+)/$', views.my_delete, name='my_delete'),

    url(r'^join/$', views.join, name='join'),

    #탈퇴
    url(r'^user_delete_confirm/$', DeleteConfirm.as_view(), name='user_delete_confirm'),
    url(r'^user_delete/$', delete_user, name='user_delete'),
    
    #비번변경
    url(r'^changepw/$', ChangePw, name='change_pw'),

    #이메일찾기
    url(r'^searchemail/$', SearchEmail.as_view(), name='search_email'),
    url(r'^findusername/$', find_username, name='find_username'),

    #비번찾기
    url(r'^searchpassword/$', SearchPassword.as_view(), name='search_password'), #폼 보여주는 템플릿
    url(r'^findpassword/$', FindPassword, name='find_password'),#폼에서 데이터 받아와서 처리
    url(r'^ForgetChangePw/(?P<email>.+)/$', ForgetChangePw, name='ForgetChangePw'),#조회결과가 있을시 서치


    url(r'^index/$', views.index, name='index'),
    url(r'^mypage/$', views.Managment, name='Managment'),
    url(r'^mypage/PWC$', auth_views.password_change, name='password_change_done',
    	kwargs={'template_name': 'login/mypage.html'}),

    url(r'^mypage/(?P<id>.+)/$', views.account_view, name='account_view'), 
    url(r'^add/(?P<id>.+)/$', views.bankbook_new, name='bankbook_new'),
    #https://github.com/django/django/blob/1.10.6/ddjango/contrib/auth/views.py#L62
    #에 def login을 보면 기본 request받고 기본 디렉토리가 내가 설정한 것과 다르기 때문에 kwargs를 사용해 임의 지정 함
    url(r'^$', auth_views.login, name='login', 
    	kwargs={'template_name': 'login/login.html'}),
    url(r'^logout/', auth_views.logout, name='logout', 
        kwargs={'next_page': settings.LOGIN_URL}),
]
