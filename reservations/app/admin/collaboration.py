from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Collaboration


class CollaborationResource(resources.ModelResource):
    """Describe how Collaboration resources can be imported or exported"""

    class Meta:
        """Meta definition for CollaborationResource."""

        model = Collaboration
        skip_unchanged = True


class CollaborationAdmin(ImportExportModelAdmin):
    """ArtistType admin register class"""

    resource_class = CollaborationResource


admin.site.register(Collaboration, CollaborationAdmin)
