from django.db import models

# Create your models here.
class Cricketer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    jersey_no = models.IntegerField()