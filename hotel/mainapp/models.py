from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.lookups import Transform

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

    def __str__(self):
        return self.hotel_name + " - "+ self.city


class Hotel_Rooms(models.Model):
    choice = (
        ('AC','AC'),
        ('Non-AC','Non-AC'),
    )
    hotel = models.ForeignKey(Hotels, on_delete=CASCADE)
    title = models.CharField(max_length=20)
    room_image = models.ImageField(upload_to='Rooms')
    type = models.CharField(max_length=15,null=True, blank=True, choices=choice)
    price = models.PositiveIntegerField()
    bed_number = models.PositiveIntegerField()
    max_guests_allow = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)




 

class Facilities(models.Model):
    choice = (
        ('Spa','Spa'),
        ('Outdoor restaurant','Outdoor restaurant'),
        ('Poolside bar','Poolside bar'),
        ('Car parking','Car parking'),
        ('Swimming pool','Swimming pool'),
        )
    Hotel = models.ForeignKey(Hotels, on_delete=CASCADE)
    title = models.CharField(max_length=20,null=True, blank=True, choices=choice)
    def __str__(self):
        return self.title
        
