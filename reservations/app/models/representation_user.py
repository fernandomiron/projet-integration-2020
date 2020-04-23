from django.db import models
from django.contrib.auth.models import User
from .representation import Representation

class Representation_user (models.Model):
    """model definition Representation_user"""

    representation = models.ForeignKey('Representation',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    seats =models.IntegerField()

    class Meta:
        """meta for Representations_user."""

        verbose_name = "Participants à la représentation"
        verbose_name_plural = "Participants à la représentation"

        ordering = ['pk']

    def __str__(self) :
        """representation of Representation_user"""

        return "({}) {} {}".format(self.pk, self.representation, self.user)