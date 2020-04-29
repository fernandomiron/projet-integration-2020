from django.db.models.signals import post_save
#we want to get a post_save signal when a user is created
from django.contrib.auth.models import UserRegisterForm
from django.dispatch import receiver
from .models import user_profile

@receiver(post_save, sender=User)
# When a user is saved send a signal.
# the signal will be received by this receiver.
def createProfile (sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver
def saveProfile (sender,instance,**kwargs):
    instance.profile.save()
