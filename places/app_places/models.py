from django.db import models
from django.core.validators import RegexValidator

CATEGORY_CHOICE = {
    1: 'A',
    2: 'B',
    3: 'C1',
    4: 'C2',
    5: 'C3',
    6: 'D1',
    7: 'D2',
    8: 'D3'
}


class Place(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=64)
    description = models.TextField()
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True)
    url = models.URLField(null=True)
    position_lat = models.FloatField()
    position_lng = models.FloatField()
    category = models.IntegerField(choices=CATEGORY_CHOICE.items())

    @property
    def position(self):
        return "{} | {}".format(self.position_lat, self.position_lng)

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.name, self.address, self.phone_number, self.url, self.position, self.description)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "phone_number": self.phone_number,
            "url": self.url,
            "lat": self.position_lat,
            "lng": self.position_lng
        }











# class Event(models.Model):
#     name = models.CharField(max_length=128)
#     position_lat = models.DecimalField()
#     position_lng = models.DecimalField()
#     expiring_date = models.DateField(blank=True)
