from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Location, Locality


class LocationResource(resources.ModelResource):
    """Describe how Location resources can be imported or exported"""

    class Meta:
        """Meta definition for LocationResource."""

        model = Location
        skip_unchanged = True


class LocalityResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for LocalityResource."""

        model = Locality
        skip_unchanged = True


class LocationAdmin(ImportExportModelAdmin):
    """ArtistType admin register class

    Customize the appearance of the table Location in the admin database
    """

    list_display = ('pk', 'designation')
    list_display_links = ('pk', 'designation')  # to make field clickable
    search_fields = ('designation',)

    resource_class = LocationResource


class LocalityAdmin(ImportExportModelAdmin):
    """ArtistType admin register class

    Customize the appearance of the table Locality in the admin database
    """
    list_display = ('pk', 'postal_code', 'locality')
    list_display_links = ('pk', 'postal_code', 'locality') # to make field clickable
    search_fields = ('postal_code', 'locality')



    resource_class = LocalityResource


admin.site.register(Location, LocationAdmin)
admin.site.register(Locality, LocalityAdmin)
