from django.db import models

class Location(models.Model):
    locality_id = models.ForeignKey("Locality", on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=60, help_text="Short identification label")
    designation = models.CharField(max_length=60, help_text="Official designation locality")
    address = models.CharField(max_length=255, help_text="Locations Address", null=True)
    website = models.CharField(max_length=255, help_text="Website Address", null=True)
    phone = models.CharField(max_length=30, help_text="Phone number", null=True)

    def __str__(self):
        return self.locality_id + 'Slug = ' + self.slug
