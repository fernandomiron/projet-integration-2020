from django.contrib import admin
<<<<<<< HEAD
from app.models.location import Location
admin.site.register(Location)
=======

from app.models import Location, Locality


admin.site.register(Location)
admin.site.register(Locality)
>>>>>>> f2e93d55e29822447b2c0ceee3ac9617b81d92cc
