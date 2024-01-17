from django.db import models

# Create your models here.
class addingcategorydb(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    discription = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(upload_to="photos", null=True, blank=True)

class categorydb(models.Model):
    category = models.CharField(max_length=40,null=True,blank=True)
    movie = models.CharField(max_length=40,null=True,blank=True)
    director = models.CharField(max_length=40,null=True,blank=True)
    discription = models.CharField(max_length=40,null=True,blank=True)
    movieimage = models.ImageField(upload_to="photos",null=True,blank=True)
    vidio = models.FileField(upload_to="vidios",null=True,blank=True)



class topviewdb(models.Model):
    movie = models.CharField(max_length=40, null=True, blank=True)
    director = models.CharField(max_length=40, null=True, blank=True)
    discription = models.CharField(max_length=40, null=True, blank=True)
    movieimage = models.ImageField(upload_to="photos", null=True, blank=True)
    vidio = models.FileField(upload_to="vidios", null=True, blank=True)

