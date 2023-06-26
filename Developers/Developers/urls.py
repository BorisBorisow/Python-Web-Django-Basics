from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Developers.Devs.urls')),
    path('admin/', admin.site.urls, name='home_page'), # name се използва за redirect или за python code in HTML and CSS
]
