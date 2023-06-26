from my_plant_app.plants.models import Profile


def get_profile(request):
    profile = Profile.objects.first()
    return {"profile": profile}
