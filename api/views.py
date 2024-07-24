from rest_framework.decorators import api_view
from rest_framework.response import Response
from ToDoList.models import Task, TaskList
from ToDoList.serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

##################################Function Based Views##################################
# @api_view(['GET', 'POST'])
# def all_tasks(request, format = None):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data, status=201)
    
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
# @api_view(['GET','PUT','DELETE'])
# def single_task(request, pk, format = None):
#     task = get_object_or_404(Task, pk=pk)
    
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data, status= 200)
    
#     elif request.method == 'PUT': #cannot chnage object ID
#         serializer = TaskSerializer(task, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= 400)
    
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status= 204)
################################## Function Based Views##################################


##################################Class Based Views##################################
class all_tasks(APIView):
    def get(self, request, format = None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = TaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status= 400)

class single_task(APIView):
    def get_object(self, pk):
        task = get_object_or_404(Task, pk = pk)
        return task
    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= 400)
    
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status= 204)
        
