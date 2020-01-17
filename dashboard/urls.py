from django.conf.urls import include
from dashboard.views import dashboard
from dashboard.views import ReferralList,ProfileUpdate
from django.urls import path

app_name = "dashboard"
urlpatterns = [
 	path('', dashboard, name='dashboard'),
    path('referrals/', ReferralList.as_view(),name="referralList"),
    path('profile/<int:pk>/',ProfileUpdate.as_view(), name='profile_update'),
]
