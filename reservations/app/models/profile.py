from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


LANGUAGES = [
    ('EN', 'Anglais'),
    ('FR', 'Français'),
    ('NL', 'Néerlandais'),
    ('GE', 'Allemand'),
    ('SP', 'Espagnol'),
    ('IT', 'Italien'),
    ('PO', 'Portugais'),
]


class UserProfile(models.Model):
    """Model definition for UserProfile.

    The related name of the model is by default "userprofile".
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='FR')

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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates a UserProfile instance when a User instance is created

    The UserProfile instance is linked to the created User.
    """

    if created and UserProfile.objects.filter(user=instance.pk).count() == 0:
        UserProfile.objects.create(user=instance)
    else:
        raise Exception("UserProfile for {} aleady exist"
                        .format(instance.username))


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Saves the UserProfile instance its User instance is saved

    The UserProfile instance is linked to the created User.
    """

    instance.userprofile.save()
