from django.db import models


class Show(models.Model):
    """Model definition for Show."""

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=60, unique=True)
    poster = models.URLField(max_length=255, null=True, blank=True)
    bookable = models.BooleanField(default=True)
    price = models.FloatField()
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        """Meta definition for Show."""

        verbose_name = 'Show'
        verbose_name_plural = 'Shows'

    def __str__(self):
        """Unicode representation of Show."""

        return "[{}] {}".format(self.pk, self.title)

    def save(self, *args, **kwargs):
        """Save method for Show.

        Rounds the price to 2 decimals.
        """

        self.price = round(self.price, 2)
        super(Show, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Show."""
        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here


class Location(models.Model):
    """Model definition for Location."""

    designation = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    # locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
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
