from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField()
    password =models.CharField(max_length=30)

# Create your models here.
