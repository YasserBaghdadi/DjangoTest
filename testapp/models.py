from django.db import models


# Create your models here.
class ModelA(models.Model):
    name = models.CharField(max_length=255)


class ModelB(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(ModelA, on_delete=models.CASCADE)

