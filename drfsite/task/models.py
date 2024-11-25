from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True )
    time_update = models.DateTimeField(auto_now=True)
    status =  models.CharField(max_length=255)
    categories =  models.CharField(max_length=255)

    def __str__(self):
        return self.title


