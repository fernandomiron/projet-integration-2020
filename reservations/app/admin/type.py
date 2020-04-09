from django.contrib import admin

from app.models.type import Type

class TypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Type, TypeAdmin)