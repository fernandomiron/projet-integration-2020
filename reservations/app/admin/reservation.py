from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Reservation
#from app.models.show import Show, Representation


class ReservationResource(resources.ModelResource):
    """Describe how Reservation resources can be imported or exported"""

    class Meta:
        """Reservation admin register class"""

        model = Reservation
        skip_unchanged = True


class ReservationAdmin(ImportExportModelAdmin):
    """Reservation admin register class"""

    list_display = ('pk', 'get_title', 'get_time', 'seats')
    list_display_links = ('pk', 'get_title', 'get_time', 'seats') # to make field clickable
    search_fields = ('representation__show__title',)

    def get_title(self, obj):
        """ to get the show title"""
        return obj.representation.show.title
    get_title.short_description = 'titre spectacle'

    def get_time(self, obj):
        """ to get the time """
        return obj.representation.time
    get_time.short_description = 'heure spectacle'


    resource_class = ReservationResource


admin.site.register(Reservation, ReservationAdmin)
