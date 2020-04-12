from django.db import models

'''
show model
'''

class Show(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255)
    location_id = models.ForeignKey('Location',  on_delete=models.CASCADE)
    bookable = models.BooleanField()
    price=models.FloatField()

    class Meta:
        db_table = 'shows'
        verbose_name_plural = 'Shows'
        verbose_name = 'Show'

    def __str__(self):
        return 'Title : ' + self.title \
            + '\nPoster URL : ' + self.title \
            + '\nLocation ID : ' + self.location_id \
            + '\nBookable : ' + self.bookable \
            + '\nPrice : ' + self.price

