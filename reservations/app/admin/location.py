from django.contrib import admin

from app.models.location import Location

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)