from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks', views.all_tasks.as_view()),
    path('tasks/<int:pk>', views.single_task.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)