from rest_framework import serializers
from ToDoList.models import Task, TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'