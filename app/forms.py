from django import forms  
from app.models import Car
from django.forms.widgets import ClearableFileInput

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'Текущяя'
    input_text = 'Изменить'
    clear_checkbox_label = 'Удалить'

class CarForm(forms.ModelForm):
    manufacturer = forms.CharField(
        label='Производитель',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите производителя автомобиля'
            }
        )
    )
    model = forms.CharField(
        label='Модель',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите модель автомобиля'
            }
        )
    )
    release_year = forms.CharField(
        label='Год выпуска',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Введите год выпуска автомобиля'
            }
        )
    )
    gearbox = forms.TypedChoiceField(
        choices=Car.GEARBOX_CHOICES,
        label='Коробка передач',
        widget=forms.Select(
            attrs={
                'required': True,
                'class': 'form-control'
            }
        )
    )
    color = forms.CharField(
        label='Цвет',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите цвет автомобиля'
            }
        )
    )
    photo = forms.ImageField(
        label= 'Фото',
        required=False,
        widget= MyClearableFileInput(
            attrs={
                'class': 'form-control',
                'accept': '.jpg,.jpeg,.png,.gif'
            }
        )
    )
    class Meta:
        model = Car
        fields = '__all__'
