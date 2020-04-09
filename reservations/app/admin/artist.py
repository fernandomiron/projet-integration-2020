from django.contrib import admin

from app.models.artist import Artist

class ArtistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artist, ArtistAdmin)