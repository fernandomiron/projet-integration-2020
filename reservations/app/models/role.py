from django.db import models

class Role(models.Model):
    """ Definition of the model Role"""
    role = models.CharField(max_length=30)


    class Meta:
        """ Behavior of the model Role """

        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        """ conversion of Types object to String """

        return self.role
