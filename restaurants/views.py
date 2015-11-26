from django.shortcuts import render
from django.http import Http404

restaurants = [{
                "name": "mcdonalds",
                "price": "$",
                "review": "its ok",
                "rating": 3,
                "phone": "02-123-1234",
                "address": "123 fake street",
                "image": "https://igcdn-photos-a-a.akamaihd.net/hphotos-ak-xfa1/t51.2885-15/e35/11820669_781036755340552_1301778049_n.jpg"
               },
               {
                "name": "burger_king",
                "price": "$$",
                "review": "flame grilled burgers!",
                "rating": 5,
                "phone": "02-234-2345",
                "address": "124 real avenue",
                "image": "https://igcdn-photos-d-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/s750x750/sh0.08/e35/12142091_980840855305675_1952232999_n.jpg"
               },
               {
                "name": "KFC",
                "price": "$$",
                "review": "fried chicken is great!",
                "rating": 4,
                "phone": "02-345-3456",
                "address": "125 unreal court",
                "image": "https://igcdn-photos-e-a.akamaihd.net/hphotos-ak-xtf1/t51.2885-15/e35/11850418_412365505620396_1952467682_n.jpg"
               }]
# helper functions
def find_restaurant_by_name(restaurants, name):
    for restaurant in restaurants:
        if restaurant['name'] == name:
            return restaurant
        else:
            print ("찾는 정보가 없습니다.")
    return None

def filter_restaurants_by_rating(restaurants, rating):
    filtered_restaurants = []
    for restaurant in restaurants:
        print(restaurant, rating)
        if restaurant['rating'] >= rating:
            filtered_restaurants.append(restaurant)
    return filtered_restaurants


def list(request):
    return render(request, 'restaurants/list.html', {"restaurants": restaurants})

def detail(request, name):
    restaurant = find_restaurant_by_name(restaurants, name)
    return render(request, 'restaurants/detail.html', {"restaurant": restaurant})

def rating(request, value):
    rated_restaurants = filter_restaurants_by_rating(restaurants, int(value))
    print (rated_restaurants)
    return render(request, 'restaurants/rating.html', {"rated_restaurants": rated_restaurants, "value" : value})