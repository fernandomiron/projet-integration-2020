from django.db import models

'''
location model
'''

class Location(models.Model):
    slug = models.SlugField(unique=True, max_length=60)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    locality_id = models.ForeignKey('Locality', on_delete=models.CASCADE, null=True, blank=True)
    website = models.URLField(max_length=255)
    phone = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural= 'Locations'
        verbose_name = 'Location'

    def __str__(self):
        return self.designation