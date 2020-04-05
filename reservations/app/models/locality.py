from django.db import models

'''
locality model
'''

class Locality(models.Model):
    postal_code = models.CharField(unique=True, max_length=6)
    locality = models.CharField(unique=True, max_length=60)

    class Meta:
        db_table = 'localities'
        verbose_name_plural = 'Localities'
        verbose_name = 'Locality'

    def __str__(self):
        return self.postal_code + ' ' + self.locality
