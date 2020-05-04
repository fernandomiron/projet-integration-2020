from django.contrib import admin
<<<<<<< HEAD
from app.models.artist import Artist
admin.site.register(Artist)
=======

from app.models import Artist, Types

admin.site.register(Artist)
admin.site.register(Types)
>>>>>>> f2e93d55e29822447b2c0ceee3ac9617b81d92cc
