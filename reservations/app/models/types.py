from django.db import models

class Type(models.Model):
    """Type model """
    expertise =  models.CharField(max_length=60)

    class Meta:
        """  meta data """
        verbose_name = "Type"
        verbose_name_plural = "Types"
        ordering = ['expertise', 'pk']
    def __str__(self):
        """ Overloading __str__ method"""
        return " {} {} ".format(self.pk, self.expertise)
