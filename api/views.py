from rest_framework.decorators import api_view
from rest_framework.response import Response
from ToDoList.models import Task, TaskList
from ToDoList.serializers import TaskSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def all_tasks(request, format = None):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=201)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def single_task(request, pk, format = None):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status= 200)
    
    elif request.method == 'PUT': #cannot chnage object ID
        serializer = TaskSerializer(task, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= 400)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status= 204)
        
        

