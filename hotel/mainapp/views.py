from django.db.models.expressions import F
from django.http.response import JsonResponse
from django.shortcuts import render
from . models import *
from django.db.models import Q

def index(request):
    location = request.GET.get('name1')
    # print(request.GET.get('fav_language'))
    price =request.GET.get('range')
    # print(request.GET.get('cars'))

    hotels = Hotels.objects.all()

    if location:
        hotels = Hotels.objects.filter(Q(country=location)|Q(division=location)|Q(city=location)|Q(street=location))
    if price:
        hotels = Hotels.objects.filter(hotel_rooms__price__lte=price)
    if price and location:
        hotels = Hotels.objects.filter(Q(hotel_rooms__price__lte=price) & Q(Q(country=location)|Q(division=location)|Q(city=location)|Q(street=location)))

    hotels.distinct()
    return render(request, 'index.html', {'hotels':hotels})

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