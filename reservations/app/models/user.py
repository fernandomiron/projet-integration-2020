from django.db import models
from django.urls import reverse
from app.models.role import Role


class User(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email=models.EmailField(max_length=255, unique=True)
    language = models.BooleanField()
    class Meta:
        """ meta data User"""
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['pk']

    def __str__ (self):
        """ Overloading __str__ method"""
        return 'Login : ' + self.login \
        		+ '\nFirstname : ' + self.firstname \
        		+ '\nLastname : ' + self.lastname \
        		+ '\nRole ID : ' + self.roleId \
        		+ '\nLanguage : ' + self.langue \

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})
