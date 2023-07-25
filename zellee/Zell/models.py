from django.db import models

# Create your models here.
class contact(models.Model):
    number=models.IntegerField()

class query(models.Model):
    contact=models.ImageField()
    email=models.EmailField()
    message=models.CharField(max_length=2000)

class contactus(models.Model):
    name=models.CharField(max_length=200)
    contact=models.ImageField()
    email=models.EmailField()
    message=models.CharField(max_length=2000)

