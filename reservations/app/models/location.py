from django.db import models
from django.urls import reverse

class Location(models.Model):

    """ Location model definition """
    locality = models.ForeignKey("Locality", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=60, unique=True)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255, null=True)
    website = models.URLField(max_length=255, null=True)
    phone = models.CharField(max_length=30, null=True)

    """ Location meta definition """
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    """ String representation of Location """
    def __str__(self):
        return f'({self.pk}) {self.designation}'

    def get_absolute_url(self):
        return reverse("app:location-detail", kwargs={"pk": self.pk})
