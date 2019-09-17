from django.db import models

# Create your models here.
class Fabric(models.Model):
    img_name=models.CharField(max_length=50,default='xx')
    img_file=models.FileField(upload_to='images')
    img_url = models.CharField(max_length=50)
class Leather(models.Model):
    img_name=models.CharField(max_length=50,default='xx')
    img_file=models.FileField(upload_to='images/leather')
    img_url = models.CharField(max_length=50)
    # def __str__(self):
    #     return self.pic_url.name
