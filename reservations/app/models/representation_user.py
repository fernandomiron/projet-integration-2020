from django.db import models

'''
representation_user model
'''

class Representation_user(models.Model):
    representation_id = models.ForeignKey("Representation", on_delete=models.CASCADE)
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Representation User"
        verbose_name_plural = "Representation Users"

    def __str__(self):
        return self.name