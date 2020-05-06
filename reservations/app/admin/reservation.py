from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Reservation

#  Describe how Reservation resources can be imported or exported:
class ReservationResource(resources.ModelResource):

    class Meta:
        model = Reservation
        skip_unchanged = True

#  Admin integration 
class ReservationAdmin(ImportExportModelAdmin):
   resource_class = ReservationResource

admin.site.register(Reservation, ReservationAdmin)
