from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task, TaskList
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','due_datetime', 'is_done','tasklist')
    list_filter = ('is_done', 'due_datetime', 'tasklist__title')

class TaskListAdmin(admin.ModelAdmin):
    list_filter = ('title', )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)