from django.contrib import admin
from reservations.app.models import Representation, Role, Show, UserProfile, Artist, ArtistType, Collaboration,\
    Locality, Location, Represenration_user, Type

# Register your models here.

admin.site.register(Type)
admin.site.register(Represenration_user)
admin.site.register(Location)
admin.site.register(Locality)
admin.site.register(Collaboration)
admin.site.register(ArtistType)
admin.site.register(UserProfile)
admin.site.register(Show)
admin.site.register(Role)
admin.site.register(Representation)
admin.site.register(Artist)
