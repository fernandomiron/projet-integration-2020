from django.db import models

class Type(models.Model):
    type = models.CharField(max_length=60, help_text="Artist Function (job)")

    def __str__(self):
        return self.type

