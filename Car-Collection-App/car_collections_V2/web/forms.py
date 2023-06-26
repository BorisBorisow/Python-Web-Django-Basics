from django import forms

from web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(attrs={'is_hidden': True})
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(),

        }


class DeleteProfileForm(EditProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance


class BaseCarFor(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        labels = {
            "image_url": "Image URL",
        }


class CreateCarForm(BaseCarFor):
    pass


class EditCarForm(BaseCarFor):
    pass


class DeleteCarForm(BaseCarFor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
