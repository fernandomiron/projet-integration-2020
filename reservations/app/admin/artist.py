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
    """Artist admin register class

    This will customize the table Artist on the admin database
    """

    list_display = ('pk', 'firstname', 'lastname')
    list_display_links = ('pk', 'firstname', 'lastname') # to make field clickable
    search_fields = ('firstname','lastname')



    resource_class = ArtistResource


class TypesAdmin(ImportExportModelAdmin):
    """Types admin register class

    This will customize the table Artist on the admin database
    """

    list_display = ('pk', 'types')
    list_display_links = ('pk', 'types') # to make field clickable
    search_fields = ('types',)

    resource_class = TypesResource


class ArtistTypeAdmin(ImportExportModelAdmin):
    """ArtistType admin register class"""

    list_display = ('pk', 'get_firstname', 'get_lastname', 'types')
    list_display_links = ('pk', 'get_firstname', 'get_lastname', 'types') # to make field clickable
    search_fields = ('artist_type__artist__firstname', 'artist_type__artist__lastname')

    def get_firstname(self, obj):
        """ get method for the artist firstname"""
        return obj.artist_type.artist.firstname
    get_firstname.short_description = 'firstname'

    def get_lastname(self, obj):
        """ get method for the artist lastname"""
        return obj.artist_type.artist.lastname
    get_firstname.short_description = 'lastname'


    resource_class = ArtistTypeResource


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(ArtistType, ArtistTypeAdmin)
