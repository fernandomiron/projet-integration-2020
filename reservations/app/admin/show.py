from django.contrib import admin

from app.models.show import Show

class ShowAdmin(admin.ModelAdmin):
    pass
admin.site.register(Show, ShowAdmin)