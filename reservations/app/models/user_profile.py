from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    langue = models.CharField(max_length=2)

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'User\'s profile'
        verbose_name_plural = 'User\'s profiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return f'({self.pk}) Profile n° ({self.user.pk}) - {self.user.username}"'