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

task_list = views.TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = views.TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

related_tasks = views.TaskViewSet.as_view({
    'get' : 'related_tasks'
})

urlpatterns = [
    path('tasklists/<int:pk>', tasklist_detail, name='tasklist_detail'),
    path('tasklists', tasklist_list, name='taskslist_list'),
    path('tasks/<int:pk>', task_detail, name='task_detail'),
    path('tasks', task_list, name='task_list'),
    path("tasks/<slug:slug>/related-tasks", related_tasks, name='related_tasks'),
]

