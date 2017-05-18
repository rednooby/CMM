from django.conf.urls import url,include
from django.contrib import admin
from django.shortcuts import redirect

'''
##최상위 주소##
def root(request):
	return redirect('login:login')
'''
urlpatterns = [
	#url(r'^$', root, name='root'), ##최상위 주소##
	#url(r'^$', lambda r: redirect('login:login'), name='root'), ##최상위 주소##
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('login.urls')),
    url(r'^index/', include('main.urls')),
]