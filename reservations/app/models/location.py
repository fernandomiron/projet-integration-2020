from django.db import models


class Locality(models.Model):
    """Model definition for Locality."""

    postal_code = models.CharField(max_length=6, unique=True)
    locality = models.CharField(max_length=60, unique=True)

    class Meta:
        """Meta definition for Locality."""

        verbose_name = 'Localité'
        verbose_name_plural = 'Localités'

    def __str__(self):
        """Unicode representation of Locality."""

        return "[{}] {} - {}".format(self.pk, self.postal_code, self.locality)

    def get_absolute_url(self):
        """Return absolute url for Locality."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here


class Location(models.Model):
    """Model definition for Location."""

    designation = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Emplacement'
        verbose_name_plural = 'Emplacements'
        ordering = ['designation']

    def __str__(self):
        """Unicode representation of Location."""

        return "[{}] {}".format(self.pk, self.designation)

    def get_absolute_url(self):
        """Return absolute url for Location."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
