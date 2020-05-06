from django.contrib import admin
from app.models import artist, collaboration
from app.models import location, profile
from app.models import reservation, show
admin.site.register(artist, collaboration)
admin.site.register(artist, collaboration)

"""class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title','slug','price','bookable')
    fieldset= (None,{'fields':(
    'title',
    'slug',
    'price',
    'bookable'
    )}

    )"""
