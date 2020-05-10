from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import UserProfile


class UserProfileResource(resources.ModelResource):
    """Describe how UserProfile resources can be imported or exported"""

    class Meta:
        """Meta definition for UserProfileResource."""

        model = UserProfile
        skip_unchanged = True


class UserProfileAdmin(ImportExportModelAdmin):
    """UserProfile admin register class"""

    resource_class = UserProfileResource


admin.site.register(UserProfile, UserProfileAdmin)
