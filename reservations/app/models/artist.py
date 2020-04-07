from django.db import models

class Artist(models.Model):
    """ One artist's model """
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
