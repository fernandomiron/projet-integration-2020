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
    """ArtistType admin register class"""

    resource_class = LocationResource


class LocalityAdmin(ImportExportModelAdmin):
    """ArtistType admin register class"""

    resource_class = LocalityResource


admin.site.register(Location, LocationAdmin)
admin.site.register(Locality, LocalityAdmin)
