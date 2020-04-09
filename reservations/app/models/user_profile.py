from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    role_id = models.ForeignKey('Role', on_delete=models.SET_NULL,null=True)
    language = models.CharField(max_length=2)

    def __str__(self):
        return self.user

