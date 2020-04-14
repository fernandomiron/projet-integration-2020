from django.db import models
from django.urls import reverse

class RepresentationUser(models.Model):

    """ RepresentationUser model definition """
    show_id = models.ForeignKey("Locality", on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey("UserProfile", on_delete=models.SET_NULL, null=True)
    places = models.IntegerField()

    """ RepresentationUser meta definition """
    class Meta:
        verbose_name = "RepresentationUser"
        verbose_name_plural = "Representation_users"

    """ String RepresentationUser of RepresentationUser """
    def __str__(self):
        return f'({self.pk})'
