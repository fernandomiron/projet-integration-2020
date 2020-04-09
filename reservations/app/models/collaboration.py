from django.db import models

class Collaboration(models.Model):
    artist_type_id = models.ForeignKey('ArtistType', on_delete=models.SET_NULL,null=True)
    show_id = models.ForeignKey("Show", on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.pk + ' Artist Type id = ' + self.artist_type_id + 'Show id = ' + self.show_id