from django import forms
from dashboard.models import Referral
from django.forms import ModelForm

class ReferralForm(ModelForm):
	class Meta:
		model = Referral
		fields = ('first_name','last_name','email','phone_number','nationality','country_of_residense')
