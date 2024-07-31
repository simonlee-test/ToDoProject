from rest_framework import serializers
from ToDoList.models import Task, TaskList
from rest_framework import request
class TaskSerializer(serializers.ModelSerializer):
    #this check ensure that only the owner can add tasks into the tasklist during POST and PUT request
    # https://stackoverflow.com/questions/72526734/prevent-user-from-creating-instance-for-other-users
    def validate_tasklist(self, value):
        """ 
        Check that the task belongs to a tasklist of the current user.
        """
        if value not in self.context['request'].user.tasklists.all():
            raise serializers.ValidationError('Only the owner of the tasklist can edit it.')
        return value
        
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskListSerilaizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #added extra_kwargs so that 'owner' field is no longer needed in api request.
    class Meta:
        model = TaskList
        fields = '__all__'
        extra_kwargs = {'owner': {'allow_blank': True}}