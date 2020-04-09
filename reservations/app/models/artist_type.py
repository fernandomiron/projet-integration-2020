from django.db import models

class ArtistType(models.Model):
    artist_id = models.ForeignKey('Artist', on_delete=models.SET_NULL,null=True)
    type_id = models.ForeignKey("Type", on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.pk + ' artist id = ' + self.artist_id + 'type id = ' + self.type_id