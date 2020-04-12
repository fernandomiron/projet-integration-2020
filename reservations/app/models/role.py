from django.db import models

"""
role model
"""

class Role(models.Model):

    role = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role