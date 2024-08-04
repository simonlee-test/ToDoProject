from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# for class-based view, genericviews, views with mixins
# urlpatterns = [
#     path('tasks', views.all_tasks.as_view()),
#     path('tasks/<int:pk>', views.single_task.as_view())
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# used by modelviewset/viewset with router
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter(trailing_slash=False)
# router.register(r'tasks', views.TaskViewSet, basename='task')
# router.register(r'tasklists', views.TaskListViewSet, basename='tasklist')

# urlpatterns = router.urls

#used by viewset for customizable url without router
tasklist_detail = views.TaskListViewSet.as_view({
    'get': 'retrieve', 
    'put': 'update', 
    'patch': 'partial_update', 
    'delete': 'destroy'
    })

tasklist_list = views.TaskListViewSet.as_view({
    'post': 'create', 
    'get': 'list'
    })

urlpatterns = [
    path('tasklists/<int:pk>', tasklist_detail, name='tasklist_detail'),
    path('tasklists', tasklist_list, name='taskslist_list'),     
]

