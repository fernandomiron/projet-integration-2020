from django.contrib import admin

from app.models import Artist, ArtistType, Types

admin.site.register(Artist)
admin.site.register(ArtistType)
admin.site.register(Types)
