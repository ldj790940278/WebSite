from django.db import models

# Create your models here.
class User(models.Model):
    nid=models.AutoField(primary_key=True)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.pic_url.name
