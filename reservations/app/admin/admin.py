from django.contrib import admin
from reservations.app.models import Representation, Role, Show, UserProfile, Artist, ArtistTypes, Collaboration,\
    Locality, Location, RepresentationUser, Types

# Register your models here.

admin.site.register(Types)
admin.site.register(RepresentationUser)
admin.site.register(Location)
admin.site.register(Locality)
admin.site.register(Collaboration)
admin.site.register(ArtistTypes)
admin.site.register(UserProfile)
admin.site.register(Show)
admin.site.register(Role)
admin.site.register(Representation)
admin.site.register(Artist)
