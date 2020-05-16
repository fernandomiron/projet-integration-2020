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
    """ArtistType admin register class

    Customize the appearance of the table Collaboration in the admin database
    """

    list_display = ('pk', 'get_firstname', 'get_lastname', 'get_title')
    list_display_links = ('pk', 'get_firstname', 'get_lastname', 'get_title') # to make field clickable
    search_fields = ('artist_type__artist__firstname', 'artist_type__artist__lastname')

    def get_firstname(self, obj):
        """ get method for the artist firstname"""
        return obj.artist_type.artist.firstname
    get_firstname.short_description = 'Prenom artiste'

    def get_lastname(self, obj):
        """ get method for the artist lastname"""
        return obj.artist_type.artist.lastname
    get_lastname.short_description = 'Nom artiste'

    def get_title(self, obj):
        """ get the show title"""
        return obj.show.title
    get_title.short_description = 'titre spectacle'



    resource_class = CollaborationResource


admin.site.register(Collaboration, CollaborationAdmin)
