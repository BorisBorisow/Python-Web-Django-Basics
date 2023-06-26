from django import forms

from car_collection.car.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        labels = {
            "image_url": "Image URL"
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    # def save(self, commit=True):
    #     if self.instance:
    #         self.instance.delete()
    #     return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
