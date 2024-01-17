from django.db import models

# Create your models here.
class commentdb(models.Model):

    comment = models.CharField(max_length=50,null=True,blank=True)


class signupdb(models.Model):
    sname = models.CharField(max_length=30,null=True,blank=True)
    semail = models.CharField(max_length=40,null=True,blank=True)
    susername = models.CharField(max_length=30,null=True,blank=True)
    spassword = models.CharField(max_length=30,null=True,blank=True)

class contactdb(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True)
    email = models.CharField(max_length=40,null=True,blank=True)
    subject = models.CharField(max_length=40,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)



