from django.db import models

from apis.models.street import Street
from apis.models.mixin import item_upload_to


class Place(models.Model):
    RESTAURANT = 'RES'
    HOSPITAL = 'HOS'
    STORE = 'STO'
    SIGHTSEEING = 'SIG'
    HISTORICAL = 'HIS'
    CATEGORY = (
        (RESTAURANT, 'Restaurant'),
        (HOSPITAL, 'Hospital'),
        (STORE, 'Store'),
        (SIGHTSEEING, 'Sightseeing'),
        (HISTORICAL, 'Historical'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY,
    )
    street = models.ForeignKey(Street)
    description = models.TextField()
    url = models.TextField()
    address = models = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=item_upload_to)


class PlacePhoto(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=item_upload_to)


class Street(models.Model):
    name = models.CharField(max_length=255)
