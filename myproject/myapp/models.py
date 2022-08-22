from django.db import models


# Create your models here.
class VnModel(models.Model):
    vn2id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    Age = models.IntegerField()
    DOJ = models.DateField()
    DOG = models.DateField()
    Dojob = models.DateField()
