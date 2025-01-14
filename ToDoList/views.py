from rest_framework.decorators import api_view
from rest_framework.response import Response
from ToDoList.models import Task, TaskList, Author, Authorship, Book, Owner
from ToDoList.serializers import AuthorSerializer, TestingSerializer, BookSerializer, OwnerSerializer, BookOutputSerializer
from ToDoList.serializers import TaskSerializer, TaskListSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework import permissions
from django.http import HttpResponseNotAllowed
################################## Function Based Views##################################
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


################################## Class Based Views##################################
# class all_tasks(APIView):
#     def get(self, request, format = None):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many = True)
#         return Response(serializer.data)

#     def post(self, request, format = None):
#         serializer = TaskSerializer(data = request.data)
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

################################## Views With Mixins###################################
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

######################################## ModelViewsets############################################
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
        
    def get_queryset(self):
        """ 
        Only return querysets that belong to the current user during GET,PUT,PATCH and DELETE requests
        """
        return super().get_queryset().filter(tasklist__owner=self.request.user)
    
    @action(detail=False, url_name="related-tasks")
    def related_tasks(self, request: Request, slug, *args, **kwargs):
        """ 
        Returns all tasks related to a tasklist with the given slug
        """
        tasks = self.get_queryset().filter(tasklist__slug = slug)
        if tasks.exists():
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        return Response('No tasks matches the query.', status= 404)

# class TaskListViewSet(viewsets.ModelViewSet):
#     queryset = TaskList.objects.all()
#     serializer_class = TaskListSerilaizer
#     permission_classes = [permissions.IsAuthenticated]

#     #Used for POST request to create tasklist
#     def perform_create(self, serializer):
#         """
#         When calling serializer.save(), set the obj.owner to the current user

#         """
#         serializer.save(owner= self.request.user)

#     # https://stackoverflow.com/questions/22760191/django-rest-framework-permissions-for-create-in-viewset?rq=3
#     def get_queryset(self):
#         """
#         Only return querysets that belong to the current user during GET, PUT, PATCH and DELETE requests
#         """
#         return super().get_queryset().filter(owner=self.request.user)
######################################## ModelViewsets ############################################

######################################### ViewSets ################################################
class TaskListViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        tasklists = get_list_or_404(TaskList, owner = request.user)
        serializer = TaskListSerializer(tasklists, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        tasklist = get_object_or_404(TaskList, owner = request.user, pk = pk)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)
    
    def update(self, request, pk):
        tasklist = get_object_or_404(TaskList, owner = request.user, pk = pk)
        serializer = TaskListSerializer(tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= 400)
    
    def create(self, request):
        serializer = TaskListSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status=400)
    
    def partial_update(self, request, pk):
        tasklist = get_object_or_404(TaskList, owner = request.user, pk=pk)
        serializer = TaskListSerializer(tasklist, request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
     
    def destroy(self, request, pk):
        tasklist = get_object_or_404(TaskList, owner = request.user, pk = pk)
        tasklist.delete()
        return Response(status= 204)   
######################################### ViewSets ################################################
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = TestingSerializer
    
    @action(detail=False, url_name="testingAuthor", methods=["GET"])
    def testingAuthor(self, request: Request, *args, **kwargs):
        outdated_authors = Authorship.objects.values('author').distinct()
        print("outdated_authors",outdated_authors)
        outdated_books = list(Book.objects.filter(authors__in = outdated_authors).distinct())
        print("outdated_books",outdated_books)
        # print("type(outdated_books)",type(outdated_books[0]))
        # print("first book", outdated_books[0].name)
        book_values = list(Book.objects.values('name').distinct())
        print(book_values, "vlaues", type(book_values[0]))
        authors = Author.objects.all()
        # authors.delete()
        
        serializer = BookSerializer(outdated_books, many = True)
        return Response(serializer.data)

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    
    @action(detail=False, url_name="testingOwner", methods=["POST"])
    def testingOwner(self, request: Request, *args, **kwargs):
        print(request.data['owners'])
        serializer = OwnerSerializer(data= request.data, many= True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status= 400)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    output_serializer_class = BookOutputSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = self.output_serializer_class
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = self.output_serializer_class
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        output = self.output_serializer_class(instance).data
        return Response(output)
