from django.db import models

class Shows (models.Model) : 
    """model definition of Shows"""

    slug = models.CharField(max_length = 60, unique=True)
    title = models.CharField(max_length = 255)
    poster_url = models.CharField(max_length = 255)
    bookable = models.BooleanField()
    price = models.FloatField()
    description = models.CharField(max_length = 500)
    created_at = models.DateField()
    location_id = models.ForeignKey('Locations',on_delete=models.CASCADE)
    

    class Meta:
        """meta for Shows."""

        verbose_name = "Show"
        verbose_name_plural = "Shows"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.title, self.price )