from django.urls import reverse
from django.db import models
from app.models.location import Location

class Show(models.Model):
    """ Show model """
    location_id = models.ForeignKey(Location, on_delete = models.CASCADE, null=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    poster_url= models.URLField(max_length=255, null=True)
    bookable = models.BooleanField()
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField(null=True)
    class Meta:
        """ Show Meta """
        verbose_name = "Show"
        verbose_name_plural = "Shows"
        ordering = ['pk']
    def __str__ (self):
        """Overloading __str__ method"""
        return self.name
    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})
