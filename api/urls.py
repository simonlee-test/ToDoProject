from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#for class-based view, genericviews, views with mixins
# urlpatterns = [
#     path('tasks', views.all_tasks.as_view()),
#     path('tasks/<int:pk>', views.single_task.as_view())
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#used by viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash = False)
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]
