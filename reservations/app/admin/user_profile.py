from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

from app.models.user_profile import UserProfile

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_group', 'get_language')
    list_select_related = ('userprofile', )


    

    def get_group(self, instance):
        return instance.groups.all()[0].name
    get_group.short_description = 'Role'

    def get_language(self, instance):
        return instance.userprofile.langue.upper()
    get_language.short_description = 'Langue'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
