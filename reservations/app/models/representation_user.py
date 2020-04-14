from django.db import models

class Representation_user (models.Model):
    """model definition Representation_user"""

    representation_id= models.ForeignKey('Representations',on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users',on_delete=models.CASCADE)

    class Meta:
        """meta for Representations_user."""

        verbose_name = "Participants à la représentation"
        verbose_name_plural = "Participants à la représentation"

        ordering = ['pk']

    def __str__(self) :
        """representation of Representation_user"""

        return "({}) {} {}".format(self.pk, self.representation_id, self.user_id)