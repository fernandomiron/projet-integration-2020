from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Location, Locality


#  Describe how Artist resources can be imported or exported:
class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        skip_unchanged = True

#  Describe how Type resources can be imported or exported:
class LocalityResource(resources.ModelResource):

    class Meta:
        model = Locality
        skip_unchanged = True
    

#  Admin integration 
class LocationAdmin(ImportExportModelAdmin):
   resource_class = LocationResource

class LocalityAdmin(ImportExportModelAdmin):
   resource_class = LocalityResource

admin.site.register(Location, LocationAdmin)
admin.site.register(Locality, LocalityAdmin)
