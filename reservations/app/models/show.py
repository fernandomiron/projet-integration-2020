from django.db import models
from datetime import date

class Show(models.Model):

    # Show model definition 
    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255, null=True)
    bookable = models.BooleanField()
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=False, default=date.today, null=True)

    # Show meta definition 
    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    # String representation of Show 
    def __str__(self):
        return f'({self.pk}) {self.title}'
