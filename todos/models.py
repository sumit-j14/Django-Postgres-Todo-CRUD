from django.db import models


# Create your models here.

# this generate a schema
class Todo(models.Model):
    content = models.TextField()
