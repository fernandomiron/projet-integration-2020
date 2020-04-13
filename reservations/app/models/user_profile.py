from django.db import models
from django.contrib.auth.models import User

'''
user class: Extending User Model Using a One-To-One Link
'''

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)
    langue = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f'({self.pk}) Profile n° ({self.user.pk}) - {self.user.username}"'