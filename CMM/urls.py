from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^index/', include('main.urls')),
    url(r'^index/', include('django.contrib.auth.urls')),
]