from email.policy import default
from django.db import models
from django.utils.timezone import now
# Create your models here.


class Registration(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    dob = models.DateField(default=now)
    about = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    pdata = models.CharField(max_length=1000)
    author = models.CharField(max_length=255,default='none')


class Users(models.Model):
    userlist= models.CharField(max_length=255)
    passlist= models.CharField(max_length=255)


# class User(models.Model):

 