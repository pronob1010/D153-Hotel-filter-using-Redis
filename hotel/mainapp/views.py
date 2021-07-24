from django.db.models.expressions import F
from django.http.response import JsonResponse
from django.shortcuts import render
from . models import *

def index(request):
    return render(request, 'index.html', {})

def hotels_api(request):
    hotels = Hotels.objects.all()

    division = request.GET.get('division')
    print(division)
    if division:
        hotels = Hotels.objects.filter(division = division)

    # price = request.GET.get("price")
    # if price:
    #     hotels = Hotels.objects.filter(Hotel_Rooms.objects.filter(price__lte= price))
    
    hotels.distinct()
    payload = []
    for hotel in hotels:
        result = {}
        result['hotel_name'] = hotel.hotel_name
        result['hotel_description'] = hotel.hotel_description
        result['hotel_image'] = str(hotel.hotel_image)
        result['hotel_country'] = hotel.country
        result['hotel_zip_code'] = hotel.zip_code
        result['hotel_division'] = hotel.division
        result['hotel_city'] = hotel.city
        result['hotel_street'] = hotel.street

        payload.append(result)
    return JsonResponse(payload, safe=False)