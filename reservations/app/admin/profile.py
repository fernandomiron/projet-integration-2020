from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import UserProfile

#  Describe how UserProfile resources can be imported or exported:
class UserProfileResource(resources.ModelResource):

    class Meta:
        model = UserProfile
        skip_unchanged = True

#  Admin integration 
class UserProfileAdmin(ImportExportModelAdmin):
   resource_class = UserProfileResource

admin.site.register(UserProfile, UserProfileAdmin)
