from django.contrib import admin

from app.models.locality import Locality

class LocalityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Locality, LocalityAdmin)