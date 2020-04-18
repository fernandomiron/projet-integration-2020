from django.db import models
from datetime import date


class Show(models.Model):
    """ Definition of model Show """

    slug = models.SlugField(max_length=60, help_text="Short identification label", unique=True)
    title = models.CharField(max_length=255, help_text="Title Show")
    poster_url = models.URLField(max_length=255, help_text="URL poster", null=True)
    bookable = models.BooleanField(help_text="if is bookable or not", default=True)
    price = models.FloatField(help_text="Show price")
    description = models.TextField(help_text="Show description")
    created_at = models.DateField(default=date.today, help_text=" Creation Date", null=True)

    class Meta:
        """ Behavior of the model Show """

        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        """ Conversion of Show object to String """

        return "(" + self.pk + ") " + self.title
