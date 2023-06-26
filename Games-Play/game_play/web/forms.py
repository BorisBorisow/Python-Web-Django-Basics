from django import forms

from web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "age", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Profile Picture"

        }
        widgets = {

            "password": forms.PasswordInput(),
        }


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            if _ == 'password':
                # To successful delete profile , skip password input.
                continue
            field.widget.attrs['readonly'] = 'readonly'


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        labels = {
            "max_level": "Max Level",
            "image_url": "Image URL",
        }


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
