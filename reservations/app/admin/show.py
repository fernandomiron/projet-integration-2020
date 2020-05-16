from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from app.models import Representation, Show



class RepresentationResource(resources.ModelResource):
    """Describe how Representation resources can be imported or exported"""

    class Meta:
        """Meta definition for RepresentationResource."""

        model = Representation
        skip_unchanged = True


class ShowResource(resources.ModelResource):
    """Describe how Type resources can be imported or exported"""

    class Meta:
        """Meta definition for ShowResource."""

        model = Show
        skip_unchanged = True



class RepresentationAdmin(ImportExportModelAdmin):
    """Representation admin register class"""

    list_display = ('pk', 'get_title', 'time', 'get_designation')
    list_display_links = ('pk', 'get_title', 'time', 'get_designation')  # to make field clickable
    search_fields = ('show__title',)

    def get_title(self, obj):
        return obj.show.title
    get_title.short_description = 'titre spectacle'
    #get_title.admin_order_field = 'Show title'

    def get_designation(self, obj):
        return obj.location.designation
    get_designation.short_description = 'designation'

    resource_class = RepresentationResource



class ShowAdmin(ImportExportModelAdmin):
    """Show admin register class"""

    list_display = ('pk', 'title', 'price') # the
    list_display_links = ('pk','title','price') # to make field clickable
    search_fields = ('title',)



    resource_class = ShowResource


admin.site.register(Show,ShowAdmin)
admin.site.register(Representation, RepresentationAdmin)
