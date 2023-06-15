from django.db import models
from django.contrib.auth.models import User



#   USER SCHEMA
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profilePic = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    educationalQualification = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Song(models.Model):
    songName = models.CharField(max_length=255)
    artistName = models.CharField(max_length=120)
    songURL = models.URLField(max_length=255)
    thumbnail = models.URLField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.songName