from django.db import models

# Create your models here.
class Property(models.Model):
    description_text = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    street_address = models.CharField(max_length=150)
    number_of_guest = models.CharField
    price_per_night = models.CharField
    price_per_night_extra_guest = models.CharField
    bunch_of_tags = models.CharField