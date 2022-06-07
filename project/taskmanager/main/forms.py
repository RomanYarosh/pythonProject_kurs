from .models import Locomotive
from django.forms import ModelForm, TextInput, Textarea


class LocomotiveForm(ModelForm):
    class Meta:
        model = Locomotive
        fields = ['name_loc', 'type_loc', 'function_loc', 'year', 'country_loc', 'construction_speed', 'weight_loc',
                  'length_loc', 'description']
        widgets = {
            'name_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название локомотива'
            }),
            'type_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип локомотива (тепловоз / электровоз, дизель-поезд / электропоезд)'
            }),
            'function_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите назначение (грузовой / пассажирский / маневровый)'
            }),
            'year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год'
            }),
            'country_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну изготовителя'
            }),
            'construction_speed': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите конструкицонную скорость'
            }),
            'weight_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите массу локомотива'
            }),
            'length_loc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите длину локомотива'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
