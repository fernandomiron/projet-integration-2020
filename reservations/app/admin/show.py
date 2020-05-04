from django.contrib import admin
<<<<<<< HEAD
from app.models.show import Show
admin.site.register(Show)
=======

from app.models import Representation, Show

admin.site.register(Show)
admin.site.register(Representation)
>>>>>>> f2e93d55e29822447b2c0ceee3ac9617b81d92cc
