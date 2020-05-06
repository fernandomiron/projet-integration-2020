from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from app.models import Artist, Types


#  Describe how Artist resources can be imported or exported:
class ArtistResource(resources.ModelResource):

    class Meta:
        model = Artist
        import_id_fields = ('firstname',)
        skip_unchanged = True
    

#  Admin integration 
class ArtistAdmin(ImportExportActionModelAdmin):
   resource_class = ArtistResource

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Types)

