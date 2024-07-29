from rest_framework import serializers
from ToDoList.models import Task, TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskListSerilaizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = TaskList
        fields = '__all__'
        extra_kwargs = {'owner': {'allow_blank': True}}