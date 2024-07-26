from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

class User(AbstractUser):
    pass

class TaskList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, default= uuid.uuid4)    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
    
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
