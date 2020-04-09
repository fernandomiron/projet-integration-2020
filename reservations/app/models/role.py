from django.db import models


class Role (models.Model):
    role = models.CharField(max_length=30)
    class Meta:
    	"""meta data Role"""
    	verbose_name = "Role"
    	verbose_name = "Roles"
    def __str__ (self):
        """Overloading __str__ method"""

        return " {} {} ".format(self.pk, self.role)
