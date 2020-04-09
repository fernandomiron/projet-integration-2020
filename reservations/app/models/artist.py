from django.db import models

class Artist(models.Model):
    firstname = models.CharField(max_length=60, help_text="Artist firstname")
    lastname = models.CharField(max_length=60, help_text="Artist lastname")

    def __str__(self):
        return self.firstname + '' + self.lastname
