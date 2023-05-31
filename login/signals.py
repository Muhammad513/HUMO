from django.dispatch import Signal,receiver
from django.db.models.signals import post_delete,post_save
from .models import Profile
from homes.models import*
from django.contrib.auth.models import User






@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    user=instance
    if created:
        Profile.objects.create(user=user,firs_name=user.first_name,last_name=user.last_name)
        


@receiver(post_delete,sender=Profile)
def profile_delete(sender,instance,**kwargs):
    profile=instance
    user=profile.user
    user.delete()        
   
        
