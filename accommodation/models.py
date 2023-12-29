from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Accommodation(models.Model):
    """
    Accommodation Model
    """
    ACCOMMODATION_TYPES = [
        ('Flat', 'Flat'),
        ('Room', 'Room'),
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    accommodation_type = models.CharField(
        max_length=20, choices=ACCOMMODATION_TYPES, default='Flat')
    accommodation_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
