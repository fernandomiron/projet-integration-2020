from django.db import models

class RepresentationUser(models.Model):
    """ Representation user model """

    representation_id = models.ForeignKey("Representation", on_delete=models.CASCADE)
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Representation User"
        verbose_name_plural = "Representation Users"

    def __str__(self):
        return f'({self.pk}) Representation ID: ({self.representation_id})  {self.user_id}'
