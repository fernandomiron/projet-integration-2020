from django.db import models
from django.urls import reverse

class Artist_type(models.Model):

    artist_id = models.ForeignKey("Artist", on_delete=models.CASCADE)
    type_id = models.ForeignKey("Type", on_delete=models.CASCADE)

    class Meta:
        db_table = "artist_type"
        verbose_name = "Artist_type"
        verbose_name_plural = "Artist_types"

    def __str__(self):
        return 'Artist : ' + self.artist_id + '\nType : ' + self.type_id

    def get_absolute_url(self):
        return reverse("Artist_type_detail", kwargs={"pk": self.pk})
