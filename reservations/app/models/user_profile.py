from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model) : 
    """model definition of Users"""

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.ForeignKey('Role',on_delete=models.CASCADE)
    langue=models.CharField(max_length=2)
    

    class Meta:
        """meta for Users."""

        verbose_name = "User"
        verbose_name_plural = "Users"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({})".format(self.pk )