from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=100, help_text='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, help_text='Last Name',widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    email = forms.EmailField(max_length=150, help_text='Email',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    date_of_birth = forms.DateField(help_text="Date of Birth",widget=forms.TextInput(attrs={'placeholder': 'Date Of Birth'}))
    nationality = forms.CharField(max_length = 100,help_text = "Nationality",widget=forms.TextInput(attrs={'placeholder': 'Nationality'}))
    country_of_residense = forms.CharField(max_length = 100, help_text = "Country Of Residense",widget=forms.TextInput(attrs={'placeholder': 'Country Of Residense'}))
    year_of_previous_yatra_attended = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Year Of Previous Yatra Attended'}))
    ACN_of_previous_yatra_attended = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ACN of Yatra Attended'}))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name','email', 'password1', 'password2',
            'date_of_birth','nationality','country_of_residense','year_of_previous_yatra_attended',
            'ACN_of_previous_yatra_attended',
                )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),            
        
        }
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})    
        