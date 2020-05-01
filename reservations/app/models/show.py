from django.db import models

from app.models.location import Location


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

        verbose_name = 'Spectacle'
        verbose_name_plural = 'Spectacles'

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


class Representation(models.Model):
    """Model definition for Representation."""

    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Representation."""

        verbose_name = 'Représentation'
        verbose_name_plural = 'Représentations'
        ordering = ['time', 'show']

    def __str__(self):
        """Unicode representation of Representation."""

        return "[{}] {} le {} à {}".format(self.pk, self.show.title, self.time,
                                           self.location.designation)

    def get_absolute_url(self):
        """Return absolute url for Representation."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
