from django.db import models
from django.urls import reverse

class User(models.Model):

    role_id = models.ForeignKey("Role", on_delete=models.CASCADE)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    langue = models.CharField(max_length=2)

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return 'Login : ' + self.login \
                + '\nFirstname : ' + self.firstname \
                + '\nLastname : ' + self.lastname \
                + '\nEmail : ' + self.email \
                + '\nRole ID : ' + self.role_id \
                + '\nLangue : ' + self.langue \

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
