from django.contrib.auth.models import User
from django.db import models


LANGUAGES = [
    ('EN', 'English'),
    ('FR', 'French'),
    ('NL', 'Dutch'),
    ('GE', 'German'),
    ('SP', 'Spanish'),
    ('IT', 'Italian'),
    ('PO', 'Portuguese'),
]


class UserProfile(models.Model):
    """Model definition for UserProfile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGES)

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'Profil d\'utilisateur'
        verbose_name_plural = 'Profils d\'utilisateur'
        ordering = ['user']

    def __str__(self):
        """Unicode representation of UserProfile."""

        return "[{}] Profile de {}".format(self.pk, self.user.username)

    def get_absolute_url(self):
        """Return absolute url for UserProfile."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
