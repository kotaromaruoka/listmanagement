from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    nottodo = models.CharField(max_length=100)
    starttime = models.CharField(max_length=100)
    endtime = models.CharField(max_length=100)
    progress = models.CharField(max_length=100,default='incomplete')
    memo = models.TextField(null=True, blank=True,default='')