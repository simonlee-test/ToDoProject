from django.contrib import admin
from .models import Task, TaskList, Authorship, Book, Author, Owner

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','due_datetime', 'is_done','tasklist')
    list_filter = ('is_done', 'due_datetime', 'tasklist__title')

class TaskListAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    # prepopulated_fields = ({'slug': ('title',)})
    readonly_fields = ('slug', )
    
class AuthorshipAdmin(admin.ModelAdmin):
    list_display = ('author', 'book')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'start_date')
    
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name','id')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Authorship, AuthorshipAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Owner, OwnerAdmin)