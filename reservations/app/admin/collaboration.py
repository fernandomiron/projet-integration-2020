from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Collaboration

#  Describe how Collaboration resources can be imported or exported:
class CollaborationResource(resources.ModelResource):

    class Meta:
        model = Collaboration
        skip_unchanged = True

#  Admin integration 
class CollaborationAdmin(ImportExportModelAdmin):
   resource_class = CollaborationResource

admin.site.register(Collaboration, CollaborationAdmin)
