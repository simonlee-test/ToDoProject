from rest_framework import serializers
from ToDoList.models import Task, TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'