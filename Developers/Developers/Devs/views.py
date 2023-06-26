from django.http import HttpResponse
from django.shortcuts import render, redirect

from Developers.Devs.models import Developer


def home_page(request):
    # developers = Developer.objects.all().order_by('-id') # подрежда данните по ид -ид наобратно
    # developers = Developer.objects.all().filter(id__gte=1)
    developers = Developer.objects.all()
    context = {
        'developers': developers,

    }
    return render(request, 'index.html', context)


def some(request):
    g = request.Get.get('g')
    print(g)
    redirect('home')
