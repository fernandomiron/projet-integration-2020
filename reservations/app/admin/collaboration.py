from django.contrib import admin

from app.models.collaboration import Collaboration

class CollaborationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Collaboration, CollaborationAdmin)