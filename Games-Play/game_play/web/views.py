from django.shortcuts import render, redirect

from web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, ProfileEditForm, \
    ProfileDeleteForm
from web.models import Profile, Game


# Create your views here.
def get_profile():
    try:
        profile = Profile.objects.first()
        return profile
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()
    context = {"profile": profile}
    return render(request, 'home/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = get_profile()
    context = {"games": games}
    return render(request, 'home/dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {"profile": profile, "form": form}

    return render(request, 'games/create-game.html', context)


def details_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    context = {"profile": profile, "game": game}
    return render(request, 'games/details-game.html', context)


def edit_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        form.save()
        return redirect("dashboard")

    context = {
        "profile": profile,
        "game": game,
        "form": form,
    }
    return render(request, 'games/edit-game.html', context)


def delete_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/delete-game.html', context)


def create_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    average_rating = sum([g.rating for g in games]) / len(games) if len(games) > 0 else 0.0

    context = {
        'games': games,
        'average_rating': average_rating,
        "profile": profile
    }
    return render(request, 'profile/details-profile.html', context)
