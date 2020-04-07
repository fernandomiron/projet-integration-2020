from django.db import models

class Users (models.Model) : 
    """model definition of Users"""

    login = models.IntegerField()
    password = models.CharField(max_length=60)
    role_id=models.ForeignKey('Roles', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    langue = models.BooleanField()

    class Meta:
        """meta for Users."""

        verbose_name = "User"
        verbose_name_plural = "Users"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.lastname, self.firstname )