from django.db import models

class Role(models.Model):

    """ Role model definition """
    role = models.CharField(max_length=30)

    """ Role meta definition """
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    """ String representation of Role """
    def __str__(self):
        return f'({self.pk}) {self.role}'
