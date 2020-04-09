from django.db import models

class Locality(models.Model):
    post_code = models.CharField(max_length=6, help_text="Postal Code")
    locality = models.TextField(max_length=60, help_text="Official designation locality")

    def __str__(self):
        return self.locality + ' ' + self.post_code

