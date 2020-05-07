from django.contrib import admin

from .show import Show

class ReservationAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'poster', 'price')

admin.site.register(Show )
