from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')


admin.site.register(User, CustomUserAdmin)
