from django.urls import path

from car_collection.profile_car.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('create/', profile_create, name="create-profile"),
    path('details', profile_details, name="profile-details"),
    path('edit/', profile_edit, name="edit-profile"),
    path('delete/', profile_delete, name="delete-profile"),
]