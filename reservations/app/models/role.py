from django.db import models
from django.urls import reverse

class Role(models.Model):

    role = models.CharField(max_length=30)

    class Meta:
        db_table = "roles"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role

    def get_absolute_url(self):
        return reverse("Role_detail", kwargs={"pk": self.pk})
