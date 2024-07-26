from rest_framework.decorators import api_view
from rest_framework.response import Response
from ToDoList.models import Task, TaskList
from ToDoList.serializers import TaskSerializer, TaskListSerilaizer
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
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
# class all_tasks(APIView):
#     def get(self, request, format = None):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format = None):
#         serializer = TaskSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= 201)
#         return Response(serializer.errors, status= 400)

# class single_task(APIView):
#     def get_object(self, pk):
#         task = get_object_or_404(Task, pk = pk)
#         return task
    
#     def get(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     #will return 404 if the targeted object does not exist for modification.
#     def put(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= 400)
    
#     def delete(self, request, pk, format=None):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status= 204)
################################## Class Based Views##################################

##################################Views With Mixins###################################
# class all_tasks(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class single_task(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
################################## Views With Mixins###################################


# ################################## Views With GenericViews###################################
# class all_tasks(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
# class single_task(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
################################## Views With GenericViews###################################

########################################Viewsets############################################
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
########################################Viewsets############################################

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerilaizer
    
    @action(detail=False, url_path=r'related-tasks/(?P<tasklist_title>\w+)', url_name="related-tasks")
    def related_tasks(self, request: Request, tasklist_title, *args, **kwargs):
        tasks = get_list_or_404(TaskList, )
        tasks = Task.objects.filter(tasklist__title = tasklist_title)
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    