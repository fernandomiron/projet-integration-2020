from django.contrib import admin

from app.models.representation import Representation

class RepresentationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Representation, RepresentationAdmin)