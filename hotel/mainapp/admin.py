from django.contrib import admin
from . models import Hotels, Hotel_Rooms, Facilities


class Hotel_RoomsAdmin(admin.TabularInline):
    model = Hotel_Rooms

class FacilitiesAdmin(admin.TabularInline):
    model = Facilities

class AllAdmin(admin.ModelAdmin):
    inlines  = [ Hotel_RoomsAdmin, FacilitiesAdmin]

admin.site.register(Hotels, AllAdmin)