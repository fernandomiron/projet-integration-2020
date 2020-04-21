from django.db import models

class RepresentationUser(models.Model):
    """ Representation user model """

    representation_id = models.ForeignKey("Representation", on_delete=models.CASCADE)
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    seats = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Representation User"
        verbose_name_plural = "Representation Users"

    def __str__(self):
        return " {} {} {} {}".format(self.pk, self.representation_id, self.user_id, self.seats)
