from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Representation, Show


class RepresentationResource(resources.ModelResource):
    """Describe how Representation resources can be imported or exported"""

    class Meta:
        """Meta definition for RepresentationResource."""

        model = Representation
        skip_unchanged = True


class ShowResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for ShowResource."""

        model = Show
        skip_unchanged = True


class RepresentationAdmin(ImportExportModelAdmin):
    """Representation admin register class"""

    resource_class = RepresentationResource


class ShowAdmin(ImportExportModelAdmin):
    """Show admin register class"""

    resource_class = ShowResource


admin.site.register(Show, ShowAdmin)
admin.site.register(Representation, RepresentationAdmin)
