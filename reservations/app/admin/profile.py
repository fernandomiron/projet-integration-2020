from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app.models import UserProfile


class UserProfileInline(admin.StackedInline):
    """Define an inline admin descriptor for UserProfile model """

    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    """Override of the default UserAdmin"""

    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
