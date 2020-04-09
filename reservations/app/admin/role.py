from django.contrib import admin

from app.models.role import Role

class RoleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Role, RoleAdmin)