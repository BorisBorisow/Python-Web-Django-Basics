from django.urls import path

from Developers.Devs import views

urlpatterns = [
    path('', views.home_page, name="home"), # '' == localhost:8000
    path('hi', views.some)
]