from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """ Definition of model Representation """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=2)

    class Meta:
        """ Behavior of the model Representation """

        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        """ Conversion of Representation object to String """

        return self.user

