from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class userimage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()


class interests(models.Model):
    senduser = models.CharField(max_length=50)
    aduser = models.CharField(max_length=50)
    product = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class shop(models.Model):
    user = models.CharField(max_length=40)
    product = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    file = models.FileField()
    Name = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    about = models.TextField()
    class Meta:
        ordering = ["-date_added"]


