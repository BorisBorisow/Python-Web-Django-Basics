from django.shortcuts import render

from car_collection.car.models import Car
from car_collection.profile_car.models import Profile


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context= {
        "cars": cars,
        "profile": profile
    }
    return render(request, 'common/catalogue.html', context)