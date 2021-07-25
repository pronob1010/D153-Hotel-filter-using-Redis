from django.http.response import JsonResponse
from django.shortcuts import render
from . models import *
from django.db.models import Q


#CACHE CONFIG:
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL',DEFAULT_TIMEOUT)

def index(request):
    location = request.GET.get('name1')
    # print(request.GET.get('fav_language'))
    price =request.GET.get('range')
    # print(request.GET.get('cars'))
    
    hotels = Hotels.objects.all()
    facilities = Facilities.objects.all()
    facilities_keys = set([i.title for i in facilities])
    # print(facilities_keys)



    if cache.get(location):
        print("from Cache")
        hotels = cache.get(location)
        
    if cache.get(price):
        print("from Cache")
        hotels = cache.get(price)
   


    elif(location,price):
        print("from DB")
        if price and location:
            hotels = Hotels.objects.filter(Q(hotel_rooms__price__lte=price) & Q(Q(country=location)|Q(division=location)|Q(city=location)|Q(street=location)))
            cache.set(price,hotels)
            cache.set(location,hotels)
        if location:
            hotels = Hotels.objects.filter(Q(country=location)|Q(division=location)|Q(city=location)|Q(street=location))
            cache.set(location, hotels)
        if price:
            hotels = Hotels.objects.filter(hotel_rooms__price__lte=price)
            cache.set(price, hotels)
                    # cache.set(price,location, hotels)
        
        hotels.distinct()
    return render(request, 'index.html', {'hotels':hotels, 'facilities':facilities_keys})

def hotels_api(request):
    hotels = Hotels.objects.all()

    division = request.GET.get('division')
    print(division)
    if division:
        hotels = Hotels.objects.filter(division = division)

    price = request.GET.get("price")
    if price:
        hotels = Hotels.objects.filter(hotel_rooms__price__lte= price)
    
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