from django.db import models

class Shows (models.Model) : 
    """model definition of Shows"""

    slug = models.CharField(max_length = 60)
    title = models.CharField(max_length = 255)
    poster_url = models.CharField(max_length =255)
    bookable = models.BooleanField
    price = models.IntegerField
    description = models.CharField(max_length = 1000)
    created_at = models.DateField


    class Meta:
        """meta for Shows."""

        verbose_name = "Show"
        verbose_name_plural = "Shows"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.title, self.price )