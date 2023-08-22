from django.db import models

# Create your models here.
class App(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)