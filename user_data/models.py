from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User as mainUser
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
    
class profile(models.Model):
    user=models.OneToOneField(mainUser,related_name="profile", on_delete=models.CASCADE)
    picture= models.FileField(blank=True, null=True,upload_to='profile')
    description= models.TextField(blank=True, null=True)

    # def save(self,*args,**kwargs):
    #     print('all done')
    #     return super().save(*args,**kwargs)