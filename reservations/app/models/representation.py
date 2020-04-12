from django.db import models
from datetime import datetime

'''
representation model
'''

class Representation(models.Model):
    
    show_id = models.ForeignKey('Show', on_delete=models.CASCADE, null=True, blank=True)
    when = models.DateTimeField()
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True )

    class Meta:
        verbose_name = "Representation"
        verbose_name_plural = "Representations"

    def __str__(self):
        return f'({self.pk}) Show ID : {self.show_id}, When : {self.when} Location ID : {self.location_id}'