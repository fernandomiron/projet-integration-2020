from django.db import models


class Representation(models.Model):

    """ Representation model definition """
    show = models.ForeignKey("Show", on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    users = models.ManyToManyField("UserProfile", through='RepresentationUser')
    
    """ Representation meta definition """
    class Meta:
        verbose_name = "Representation"
        verbose_name_plural = "Representations"

    """ String representation of Representation """
    def __str__(self):
        return f'({self.pk})'
