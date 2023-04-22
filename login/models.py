from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import os
from django.db import transaction
from .choices import*
def get_image_path(instance,filename):
    return os.path.join('img', str(instance.user.id),filename)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    firs_name=models.CharField(max_length=20,blank=True,default='XXXX')
    last_name=models.CharField(max_length=20,blank=True,default='XXXX')
    pic=models.ImageField(upload_to=get_image_path,default='img/default.jpg')
    activate=models.BooleanField(default=False)
        
   
