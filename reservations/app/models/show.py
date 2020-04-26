from django.db import models

class Show (models.Model) : 
    """model definition of Shows"""

    
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 60, unique=True)
    
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True,null=True,blank=True)
    poster_url = models.CharField(max_length = 255, null=True,blank=True)
    bookable = models.BooleanField(default=True)
    price = models.FloatField()

    

    class Meta:
        """meta for Shows."""

        verbose_name = "Show"
        verbose_name_plural = "Shows"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.title, self.price )
