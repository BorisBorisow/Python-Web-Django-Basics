from django.shortcuts import render, redirect

from web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, DeleteProfileForm
from web.models import Profile, Car


# Create your views here.
def get_profile():
    return Profile.objects.first()


def index(request):
    profile = get_profile()
    context = {
        "profile": profile
    }
    return render(request, 'common/index.html', context)


def get_cars():
    return Car.objects.all()


def catalogue(request):
    cars = get_cars()
    profile = get_profile()
    context = {"cars": cars, "profile": profile}
    return render(request, 'common/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "form": form,
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    cars = get_cars()
    total_sum = sum([car.price for car in cars])
    context = {
        "profile": profile,
        "cars": cars,
        "total_sum": total_sum,
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    cars = get_cars()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()

        for car in cars:
            car_form = DeleteCarForm(request.POST, instance=car)
            car_form.save()

        return redirect('index')

    context = {
        'profile': profile
    }

    return render(request, 'profile/profile-delete.html', context)


def car_create(request):
    profile = get_profile()
    form = CreateCarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {'form': form, "profile": profile}
    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()
    context = {'profile': profile, "car": car}
    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()

    if request.method == "POST":
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)

    context = {'form': form, "car": car, "profile": profile}
    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "car": car,
        "form": form,
    }
    return render(request, 'car/car-delete.html', context)
