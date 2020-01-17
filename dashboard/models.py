from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]
# Create your models here.
class Referral(models.Model):
    referred_by = models.ForeignKey(User,on_delete=models.SET(get_sentinel_user),blank = True, null = True,related_name='referrals')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)
    phone_number = models.CharField(max_length=30)
    nationality = models.CharField(max_length = 50)
    country_of_residense = models.CharField(max_length = 50)
    def __str__(self):
    	return self.first_name