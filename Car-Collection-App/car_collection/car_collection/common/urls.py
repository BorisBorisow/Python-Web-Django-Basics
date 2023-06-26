from django.urls import path

from car_collection.common.views import index, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
]