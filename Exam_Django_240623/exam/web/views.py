from django.shortcuts import render, redirect

from web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, ProfileDeleteForm, \
    EditProfileForm
from web.models import Profile, Fruit


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist as ex:
        return None


def get_fruits():
    try:
        fruits = Fruit.objects.all()
        return fruits
    except Profile.DoesNotExist as ex:
        return None


# Create your views here.
def index(request):
    profile = get_profile()
    context = {"profile": profile}
    return render(request, 'common/index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all()
    profile = get_profile()
    context = {
        "fruits": fruits,
        "profile": profile,
    }
    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    if request.method == "GET":
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form, }
    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "fruit": fruit,
        "form": form,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    fruits = get_fruits()
    fruits_length = len(fruits)

    context = {
        "profile": profile,
        "fruits": fruits,
        "fruits_length": fruits_length,
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html',context)


def delete_profile(request):
    # profile = get_profile()
    #
    # if request.method == 'GET':
    #     form = ProfileDeleteForm(instance=profile)
    # else:
    #     form = ProfileDeleteForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #
    # context = {'form': form, 'profile': profile}
    # return render(request, 'profile/delete-profile.html', context)
    profile = get_profile()
    fruits = get_fruits()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for fruit in fruits:
            fruit_form = DeleteFruitForm(request.POST, instance=fruit)
            fruit_form.save()
        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context)