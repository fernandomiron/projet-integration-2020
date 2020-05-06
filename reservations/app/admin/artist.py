from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Artist, Types


#  Describe how Artist resources can be imported or exported:
class ArtistResource(resources.ModelResource):

    class Meta:
        model = Artist
        skip_unchanged = True

#  Describe how Artist resources can be imported or exported:
class TypesResource(resources.ModelResource):

    class Meta:
        model = Types
        skip_unchanged = True
    

#  Admin integration 
class ArtistAdmin(ImportExportModelAdmin):
   resource_class = ArtistResource

class TypesAdmin(ImportExportModelAdmin):
   resource_class = TypesResource

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Types, TypesAdmin)

