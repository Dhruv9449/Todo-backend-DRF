from nturl2path import url2pathname
from pyexpat import model
from subprocess import CompletedProcess
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(null=True, default=False)
    url = models.URLField(max_length=100, null=True, default=None)
    order = models.IntegerField(null=True, default=None)
