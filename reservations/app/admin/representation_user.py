from django.contrib import admin

from app.models.representation_user import RepresentationUser

class RepresentationUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(RepresentationUser, RepresentationUserAdmin)