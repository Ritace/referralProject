from django.contrib import admin

from dashboard.models import Referral
# Register your models here.
import csv
from django.http import HttpResponse
import sys

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class ReferralAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('first_name', 'last_name','email')
    actions = ["export_as_csv"]
    list_per_page = sys.maxsize
    pass
admin.site.register(Referral,ReferralAdmin)
