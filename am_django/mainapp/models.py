from django.db import models

class Client(models.Model):

    def __str__(self):
        return self.email
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    message = models.CharField(max_length=500)
    phone = models.IntegerField()

    read = models.BooleanField(default=False)

class Company(models.Model):

    def __str__(self):
        return self.email

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    message = models.CharField(max_length=500)
    phone = models.IntegerField()

    read = models.BooleanField(default=False)