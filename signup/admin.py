from django.contrib import admin

from signup.models import Profile
from dashboard.admin import ExportCsvMixin
import sys
# Register your models here.


class ProfileAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ('first_name', 'last_name','email')
    actions = ["export_as_csv"]
    list_per_page = sys.maxsize
    pass
admin.site.register(Profile, ProfileAdmin)