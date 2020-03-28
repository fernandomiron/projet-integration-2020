from django.db import models
from django.urls import reverse

class Type(models.Model):
    type = models.CharField(max_length=60)    

    class Meta:
        db_table = "types"
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("Type_detail", kwargs={"pk": self.pk})

