from django.shortcuts import render, redirect

from my_plant_app.plants.forms import ProfileCreateForm, CreatePlantForm, EditPlantForm, DeletePlantForm, \
    EditProfileForm
from my_plant_app.plants.models import Plant, Profile


# Create your views here.
def home_page(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {"plants": plants}
    return render(request, 'common/catalogue.html', context=context)


def create_plant(request):
    form = CreatePlantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        "form": form,
    }

    return render(request, 'plants/create-plant.html', context=context)


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).first()
    context = {
        "plant": plant,
    }

    return render(request, 'plants/plant-details.html', context=context)


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = EditPlantForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        "form": form,
        "plant": plant
    }

    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    # form = DeletePlantForm(request.POST or None, instance=plant)
    # if form.is_valid():
    #     form.save()
    #     return redirect('catalogue')
    #
    # context = {
    #     "form": form,
    #     plant: plant,
    # }
    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'plant': plant,
        'form': form
    }
    return render(request, 'plants/delete-plant.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {"form": form}

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    plants = Plant.objects.all()

    context = {"plants": plants}
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("profile_details")

    context = {
        "form": form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect("home-page")

    return render(request, 'profile/delete-profile.html')