from django.db import models
from django.urls import reverse
from app.models.locality import Locality

class Location(models.Model):
    """Location model"""
    locality_id = models.ForeignKey(Locality, on_delete = models.CASCADE, null=True)
    slug = models.SlugField(max_length=60, unique = True)
    designation = models.CharField(max_length=60)
    adress = models.CharField(max_length=255, null=True)
    website = models.URLField(max_length=255, null=True)
    phone = models.CharField(max_length=30, null=True)
    class Meta:
        """ Location meta"""
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})

    def __str__(self):
        """ Overloading __str__ method"""
        return " {} {} {} {} {} {}".format(self.locality_id, self.slug, self.designation, self.adress, self.website, self.phone)
