from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_plant_app.plants.urls')),
    path('admin/', admin.site.urls),
]
