from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('z_backup_login.urls')),
    url(r'^login/', include('login.urls')),
]
