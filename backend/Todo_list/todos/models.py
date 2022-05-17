from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title
