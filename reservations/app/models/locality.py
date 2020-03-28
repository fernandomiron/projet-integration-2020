from django.db import models
from django.urls import reverse

class Locality(models.Model):

    postal_code = models.CharField(max_length=6, unique=True)
    locality = models.CharField(max_length=60)

    class Meta:
        db_table = "localities"
        verbose_name = "Locality"
        verbose_name_plural = "Localities"

    def __str__(self):
        return self.postal_code + ' ' + self.locality

    def get_absolute_url(self):
        return reverse("Locality_detail", kwargs={"pk": self.pk})
