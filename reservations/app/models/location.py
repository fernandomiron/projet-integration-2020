from django.db import models

'''
location model
'''

class Location(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    locality_id = models.ForeignKey('Locality', on_delete=models.SET_NULL, null=True)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    class Meta:
        db_table = 'locations'
        verbose_name_plural= 'Locations'
        verbose_name = 'Location'

    def __str__(self):
        return 'Designation: ' + self.designation \
            + '\nAddress: ' + self.address \
            + '\nLocality ID: ' + self.locality_id \
            + '\nWelbsite : ' + self.website \
            +'\nPhone : ' + self.phone         
