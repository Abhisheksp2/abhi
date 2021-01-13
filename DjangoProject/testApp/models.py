from django.db import models

# Create your models here.

# added comment
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    phonenumber = models.BigIntegerField()

class Employee(models.Model):
    pass
