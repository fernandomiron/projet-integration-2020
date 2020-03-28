from django.db import models
from django.urls import reverse
from datetime import date

class Show(models.Model):

    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255, null=True)
    bookable = models.BooleanField()
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=False, default=date.today, null=True)

    class Meta:
        db_table = "shows"
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        return 'Title : ' + self.title \
                + '\nSlug : ' + self.slug \
                + '\nPoster URL : ' + self.poster_url \
                + '\nBookable : ' + self.bookable \
                + '\nPrice : ' + self.price \
                + '\nDescription : ' + self.description \
                + '\nCreated at : ' + self.created_at 

    def get_absolute_url(self):
        return reverse("Show_detail", kwargs={"pk": self.pk})
