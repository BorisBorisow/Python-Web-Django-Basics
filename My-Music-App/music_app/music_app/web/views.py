from django.shortcuts import render, redirect

from music_app.web.forms import ProfileCreateForm, CreateAlbumForm, DeleteAlbumModelForm
from music_app.web.models import Profile, Album


# Create your views here.


def home_page(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = ProfileCreateForm()

    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(request.path_info)

    context = {"albums": albums, "add_form": form}

    if profile:
        template = "home/home-with-profile.html"
    else:
        template = "home/home-no-profile.html"

    return render(request, template_name=template, context=context)


def add_album(request):
    profile = Profile.objects.first()

    if not profile:
        redirect('home page')

    form = CreateAlbumForm(request.POST or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.profile = profile
        album.save()
        return redirect("home page")

    context = {"profile": profile, "add_form": form}

    return render(request, "albums/add-album.html", context)


def album_details(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    context = {
        "profile": profile,
        "album": album,
    }
    return render(request, 'albums/album-details.html', context)


def album_edit(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = CreateAlbumForm(instance=album)
    context = {"profile": profile, "form": form, "album": album}

    if request.method == "POST":
        form = CreateAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home page")
    return render(request, 'albums/edit-album.html', context)


def album_delete(request, id):
    profile = Profile.objects.first()
    album = Album.objects.get(id=id)
    form = DeleteAlbumModelForm(instance=album)

    if request.method == "POST":
        form = DeleteAlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect("home page")

    context = {"form": form, "profile": profile, "album": album}

    return render(request, "albums/delete-album.html", context)


def profile_details(request):
    context = {
        "profile": Profile.objects.first()
    }

    return render(request, "profile/profile-details.html", context)


def profile_delete(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('home page')

    return render(request, "profile/profile-delete.html")
