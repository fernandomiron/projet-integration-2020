from django.db import models
from datetime import datetime

class representation(models.Model):
    show_id = models.ForeignKey('Show', on_delete=models.SET_NULL, null=True)
    when = models.DateTimeField(help_text="Representation Date", null=True)
    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.when
