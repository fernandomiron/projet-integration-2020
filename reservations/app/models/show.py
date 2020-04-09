from django.db import models
from datetime import date

class Show(models.Model):
    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=60, help_text="Short identification label")
    title = models.CharField(max_length=255, help_text="Title Show")
    poster_url = models.CharField(max_length=255, help_text="URL poster",null=True)
    bookable = models.BooleanField(help_text="if is bookable or not")
    price = models.FloatField(help_text="Show price")
    description = models.TextField(help_text="Show description")
    created_at = models.DateField(default=date.today, help_text=" Creation Date", null=True)

    def __str__(self):
        return self.title