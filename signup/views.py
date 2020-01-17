from django.shortcuts import render
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.profile.nationality = form.cleaned_data.get('nationality')
            user.profile.country_of_residense = form.cleaned_data.get('country_of_residense')
            user.profile.year_of_previous_yatra_attended = form.cleaned_data.get('year_of_previous_yatra_attended')
            user.profile.ACN_of_previous_yatra_attended = form.cleaned_data.get('ACN_of_previous_yatra_attended')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print("invalid form");
            
            return render(request, 'registration/signup.html', {'form': form})
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    