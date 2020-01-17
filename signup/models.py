from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank = True,null = True)
    email = models.EmailField(max_length=150,blank = True,null = True)
    nationality = models.CharField(max_length = 100,blank = True,null = True)
    country_of_residense = models.CharField(max_length = 100,blank = True,null = True)
    occupation = models.CharField(max_length = 100,blank = True,null = True)
    company = models.CharField(max_length = 100,blank = True, null = True)
    height = models.CharField(max_length = 100, blank = True, null = True)
    weight = models.CharField(max_length = 100, blank = True, null = True)
    year_of_previous_yatra_attended = models.DateField(blank = True,null = True)
    ACN_of_previous_yatra_attended = models.CharField(max_length = 100,blank = True,null = True)
    #other fields will be added here 
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



