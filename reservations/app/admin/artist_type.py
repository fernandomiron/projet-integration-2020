from django.contrib import admin

from app.models.artist_type import Artist_type

class Artist_typeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artist_type, Artist_typeAdmin)