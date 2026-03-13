from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.CharField(max_length=100) # day
    deadline = models.CharField(max_length=100) #
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
