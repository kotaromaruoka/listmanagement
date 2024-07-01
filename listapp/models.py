from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    nottodo = models.CharField(max_length=100)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    progress = models.CharField(max_length=100)
    memo = models.TextField()