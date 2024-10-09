from django.db import models
import uuid
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
# Create your models here.
from django.template.defaultfilters import slugify

class TaskList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, default= "", unique=True, null=False, editable=False)    
    owner = models.ForeignKey('User.User', related_name='tasklists', on_delete= models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    due_datetime = models.DateTimeField(blank= True, verbose_name='due date & time')
    is_done = models.BooleanField(default=False)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name= 'tasks')
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.description

class Author(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=11)

    def clean(self) -> None:
        if self.end_date < self.start_date:
            raise ValidationError("Start date cannot be later than end date")

    def save(self, *args, **kwargs) -> None:
        self.clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='authors', through='Authorship')
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, blank=True)
    
class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.author} - {self.book}"
    
class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age= models.IntegerField(null=True, blank=True, default=11)

    def __str__(self):
        return self.name
