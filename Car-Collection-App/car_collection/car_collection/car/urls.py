from django.urls import path

from car_collection.car.views import car_create, car_details, car_edit, car_delete


urlpatterns = [
    path('create/', car_create, name='create-car'),
    path('<int:pk>/details/', car_details, name='car-details'),
    path('<int:pk>/edit/', car_edit, name='edit-car'),
    path('<int:pk>/delete/', car_delete, name='delete-car'),
]