from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

class EventManager(models.Model):

    name=models.CharField(max_length=100)

    description=models.TextField()

    date=models.CharField(max_length=10)

    time=models.CharField(max_length=10)

    location=models.CharField(max_length=100)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.name

