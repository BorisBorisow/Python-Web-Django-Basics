from django import forms

from web.models import Profile, Fruit


# ---------------------------------------------Fruits ----------------------------------------------------
class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['nutrition']
        labels = {
            "image_url": "Image URL",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            "description": forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
        }


class CreateFruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Fruit
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            "description": forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            "nutrition": forms.Textarea(
                attrs={'placeholder': 'Nutrition'}
            ),
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        labels = {
            "image_url": "Image URL",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            "description": forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            "nutrition": forms.Textarea(
                attrs={'placeholder': 'Nutrition'}
            ),
        }


class DeleteFruitForm(BaseFruitForm):
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


# -------------------------------------------Profile----------------------------------------------------------------
class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email", "password"]
        labels = ""
        widgets = {
            "first_name": forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            "last_name": forms.TextInput(
                attrs={'placeholder': 'Last Name'}
            ),
            "password": forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
            "email": forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "image_url", "age"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "image_url": "Image URL",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            "last_name": forms.TextInput(
                attrs={'placeholder': 'Last Name'}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': 'Image URL'}
            ),
            "age": forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
        }


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance
