from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Representation, Show

#  Describe how Representation resources can be imported or exported:
class RepresentationResource(resources.ModelResource):

    class Meta:
        model = Representation
        skip_unchanged = True

#  Describe how Type resources can be imported or exported:
class ShowResource(resources.ModelResource):

    class Meta:
        model = Show
        skip_unchanged = True
    

#  Admin integration 
class RepresentationAdmin(ImportExportModelAdmin):
   resource_class = RepresentationResource

class ShowAdmin(ImportExportModelAdmin):
   resource_class = ShowResource

admin.site.register(Show, ShowAdmin)
admin.site.register(Representation, RepresentationAdmin)
