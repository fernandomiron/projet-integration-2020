from django.db import models

"""
type model
"""
class Type(models.Model):
    type = models.CharField(max_length=60)

    class Meta:
        db_table = 'types'
        verbose_name_plural = 'Types'
        verbose_name = 'Type'

    def __str__(self):
        return self.type