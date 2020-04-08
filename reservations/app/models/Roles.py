from django.db import models

class Roles (models.Model) : 
    """model definition of roles"""

    role = models.CharField(max_length = 30)

    class Meta:
        """meta for role."""

        verbose_name = "Role"
        verbose_name_plural = "Roles"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {}".format(self.pk, self.role)