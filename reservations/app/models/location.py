from django.db import models

from .locality import Locality


class Location(models.Model):
    """ Definition of model Location"""

    locality_id = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=60, help_text="Short identification label")
    designation = models.CharField(max_length=60, help_text="Official designation locality")
    address = models.CharField(max_length=255, help_text="Locations Address", null=True)
    website = models.URLField(max_length=255, help_text="Website Address", null=True)
    phone = models.CharField(max_length=30, help_text="Phone number", null=True)

    class Meta:
        """ Behavior of the model Locality """
        verbose_name = "location"
        verbose_name_plural = "locations"


    def __str__(self):
        """ Conversion of Locality object to String """
        return self.locality_id + 'Slug = ' + self.slug
