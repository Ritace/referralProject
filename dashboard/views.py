from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReferralForm
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from dashboard.models import Referral
from django.views.generic.edit import UpdateView
from signup.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# Create your views here.
@login_required
def dashboard(request):
    form = ReferralForm()

    
    if request.method == "POST":
    	form = ReferralForm(request.POST)
    	if form.is_valid():
    		#form is valid
            form.referred_by = request.user
            referee= form.save()
            referee.refresh_from_db()
            referee.referred_by = request.user
            referee.save()
            messages.add_message(request, messages.SUCCESS, 'SUCCESS!!Your Referral Has Been Saved.')
            return render(request, 'dashboard/dashboard.html', {'form': ReferralForm()})
    
    
    return render(request, 'dashboard/dashboard.html', {'form': form})


class ReferralList(LoginRequiredMixin,ListView):
    model = Referral    

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    
    model = Profile
    fields = ('first_name', 'last_name','email','date_of_birth','nationality','country_of_residense','year_of_previous_yatra_attended',
            'ACN_of_previous_yatra_attended',)
    
    def form_valid(self, form):
        form.save()
        return redirect('dashboard:profile_update',pk=self.request.user.id)