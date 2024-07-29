from django.contrib import admin
from .models import Task, TaskList

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','due_datetime', 'is_done','tasklist')
    list_filter = ('is_done', 'due_datetime', 'tasklist__title')

class TaskListAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    # prepopulated_fields = ({'slug': ('title',)})
    readonly_fields = ('slug', )
    

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)