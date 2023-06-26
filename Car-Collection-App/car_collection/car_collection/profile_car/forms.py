from django import forms

from car_collection.profile_car.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "email", "age", "password", ]
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            )
        }
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Picture",
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass
    # ToDo


