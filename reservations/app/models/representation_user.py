from django.db import models

class Represenration_user(models.Model):
    representation_id = models.ForeignKey('Representation', on_delete=models.CASCADE)
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    seat = models.IntegerField(help_text="Number of seats ")

    def __str__(self):
        self.seat