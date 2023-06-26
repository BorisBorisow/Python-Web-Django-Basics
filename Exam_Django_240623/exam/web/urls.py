from django.urls import path, include
from . import views
'''
•	http://localhost:8000/profile/create/ - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create fruit'),

    path('<int:pk>', include([
        path('details/', views.details_fruit, name='details fruit'),
        path('edit/', views.edit_fruit, name='edit fruit'),
        path('delete/', views.delete_fruit, name='delete fruit'),

    ])),

    path('profile/', include([
        path('craete/', views.create_profile, name='create profile'),
        path('details/', views.details_profile, name='details profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),

    ]))

]