from django import forms

from my_plant_app.plants.models import Profile, Plant


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Profile Picture",
        }


class ProfileCreateForm(BaseProfileForm):
    pass


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        labels = {
            "plant_type": "Type",
            "image_url": "Image URL",
        }


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class EditProfileForm(BaseProfileForm):
    BaseProfileForm.Meta.fields.append("profile_picture")


