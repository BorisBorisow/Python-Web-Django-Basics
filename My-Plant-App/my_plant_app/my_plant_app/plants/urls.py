from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('catalogue/', views.catalogue, name="catalogue"),

    path('create/', views.create_plant, name="create-plant"),
    path('details/<int:pk>', views.details_plant, name="details-plant"),
    path('edit/<int:pk>', views.edit_plant, name="edit-plant"),
    path('delete/<int:pk>', views.delete_plant, name="delete-plant"),

    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete')
    ]))
]

