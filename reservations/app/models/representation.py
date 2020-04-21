from django.db import models
from django.urls import reverse
from app.models.show import Show
from app.models.location import Location


class Representation(models.Model):
    """ Representation model """

    show_id = models.ForeignKey('Show', on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField()
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True )
    total_seats = models.IntegerField(default=0)
    available_seats = models.IntegerField(default=0)

    class Meta:
        """ Representation meta data """
        verbose_name = "Representation"
        verbose_name_plural = "Representations"


    def __str__(self):
        """Representation string"""
        return " {} {} {} {} {} {}".format (self.pk, self.show_id, self.time, self.location_id, self.total_seats, self.available_seats)
