from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Reservation


class ReservationResource(resources.ModelResource):
    """Describe how Reservation resources can be imported or exported"""

    class Meta:
        """Reservation admin register class"""

        model = Reservation
        skip_unchanged = True


class ReservationAdmin(ImportExportModelAdmin):
    """Reservation admin register class"""

    resource_class = ReservationResource


admin.site.register(Reservation, ReservationAdmin)
