from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True)
    dob = models.DateField()
    address = models.TextField(null=True,max_length=100)


class Car(models.Model):
    name = models.CharField(max_length=50)
    speed = models.IntegerField()