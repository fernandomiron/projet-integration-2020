from django.db import models


class Artist(models.Model):
    """Definition of the model Artist """

    firstname = models.CharField(max_length=60, help_text="Artist firstname")
    lastname = models.CharField(max_length=60, help_text="Artist lastname")

    class Meta:
        """ Behavior of the Artist model """

        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    @property
    def __str__(self):
        """ conversion of Artist object to String """

        return self.firstname + ' ' + self.lastname
