from django.shortcuts import render, redirect

from car_collection.car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from car_collection.car.models import Car


# Create your views here.
def car_create(request):
    form = CreateCarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        "form": form,
    }
    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = get_car_by_pk(pk)
    context = {"car": car}

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = get_car_by_pk(pk)
    form = EditCarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        "form": form,
        "car": car
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = get_car_by_pk(pk)
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context)


def get_car_by_pk(ident_num):
    return Car.objects.filter(pk=ident_num).get()
