from django.db import models

# Create your models here.

class Tableone(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    