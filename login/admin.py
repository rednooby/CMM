from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ['username','password1','email','birth']

admin.site.register(User, UserAdmin)