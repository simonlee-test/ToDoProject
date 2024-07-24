from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks', views.all_tasks),
    path('tasks/<int:pk>', views.single_task)
]

urlpatterns = format_suffix_patterns(urlpatterns)