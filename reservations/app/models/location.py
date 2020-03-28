from django.db import models
from django.urls import reverse

class Location(models.Model):

    locality_id = models.ForeignKey("Locality", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=60, unique=True)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255, null=True)
    website = models.URLField(max_length=255, null=True)
    phone = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "locations"
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})
