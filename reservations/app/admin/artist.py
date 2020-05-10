from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Artist, ArtistType, Types


class ArtistResource(resources.ModelResource):
    """Describe how Artist resources can be imported or exported"""

    class Meta:
        """Meta definition for ArtistResource."""

        model = Artist
        skip_unchanged = True


class TypesResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for TypeResource."""

        model = Types
        skip_unchanged = True


class ArtistTypeResource(resources.ModelResource):
    """Describe how ArtistType resources can be imported or exported"""

    class Meta:
        """Meta definition for ArtistTypeResource."""

        model = ArtistType
        skip_unchanged = True


class ArtistAdmin(ImportExportModelAdmin):
    """Artist admin register class"""

    resource_class = ArtistResource


class TypesAdmin(ImportExportModelAdmin):
    """Types admin register class"""

    resource_class = TypesResource


class ArtistTypeAdmin(ImportExportModelAdmin):
    """ArtistType admin register class"""

    resource_class = ArtistTypeResource


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(ArtistType, ArtistTypeAdmin)
