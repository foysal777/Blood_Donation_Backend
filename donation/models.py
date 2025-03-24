from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    donor_position = models.CharField(max_length=10)
    date = models.DateField()
    blood_group = models.CharField(max_length=50)  
    phone = models.CharField(max_length=15)
    donation_place = models.CharField(max_length=255)
    image_url = models.CharField(max_length=500, blank=True, null=True)  

    def __str__(self):
        return self.name
