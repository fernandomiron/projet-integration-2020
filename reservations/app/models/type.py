from django.db import models
from django.urls import reverse

class Type(models.Model):

    #Type model definition
    type = models.CharField(max_length=60)    

    #Type meta definition
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
    
    #String representation of Type
    def __str__(self):
        return f'({self.pk}) {self.type}'

