from django.db import models

class Representation_user (models.Model):
    """model definition Representation_user"""

    representation = models.ForeignKey('Representations',on_delete=models.CASCADE)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    seats =models.IntegerField(max_length=11)

    class Meta:
        """meta for Representations_user."""

        verbose_name = "Participants à la représentation"
        verbose_name_plural = "Participants à la représentation"

        ordering = ['pk']

    def __str__(self) :
        """representation of Representation_user"""

        return "({}) {} {}".format(self.pk, self.representation, self.user)