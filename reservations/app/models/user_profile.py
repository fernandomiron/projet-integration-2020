from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ UserProfile model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    langue = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f'{self.user.username} Profile'
