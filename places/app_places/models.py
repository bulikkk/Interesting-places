from django.db import models
from django.core.validators import RegexValidator


# class Place(models.Model):
#
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
#                                  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#
#     name = models.CharField(max_length=64)
#     address = models.TextField()
#     phone_number = models.CharField(validators=[phone_regex], blank=True)
#     url = models.URLField()
#     position_lat = models.DecimalField()
#     position_lng = models.DecimalField()
#
#
# class Event(models.Model):
#     name = models.CharField(max_length=128)
#     position_lat = models.DecimalField()
#     position_lng = models.DecimalField()
#     expiring_date = models.DateField(blank=True)
