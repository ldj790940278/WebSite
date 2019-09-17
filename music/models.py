from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=25)
    album_title=models.CharField(max_length=25)
    genre=models.CharField(max_length=25)
    album_logo=models.CharField(max_length=100)
class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=20)
