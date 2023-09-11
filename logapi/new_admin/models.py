from django.db import models

# Create your models here.
class RegAdmin(models.Model):
    username=models.CharField(max_length=50)
    password=models.IntegerField()