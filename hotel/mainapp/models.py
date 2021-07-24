from django.db import models
from django.db.models.deletion import CASCADE

class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField(max_length=250)
    hotel_image = models.ImageField(upload_to="Hotel")
    chech_in_From = models.TimeField()
    chech_in_To = models.TimeField()
    check_out_From = models.TimeField()
    check_out_To = models.TimeField()
    
    country = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10)
    division = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=50)


class Hotel_Rooms(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=CASCADE)
    title = models.CharField(max_length=20)
    room_image = models.ImageField(upload_to='Rooms')
    price = models.PositiveIntegerField()
    bed_number = models.PositiveIntegerField()
    max_guests_allow = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)

class Facilities(models.Model):
    Hotel = models.ForeignKey(Hotels, on_delete=CASCADE)
    title = models.CharField(max_length=20)

