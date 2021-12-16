from .models import client
from django.forms import ModelForm, TextInput, Textarea



class clientForm(ModelForm):
    class Meta:
        model = client
        fields = ["name", "task"]
        widgets = {
        "name": TextInput(attrs={
            "class":'form-control',
            "placeholder": 'Введите ваше имя'
        }),
        "task": Textarea(attrs={
            "class": 'form-control',
            "placeholder": 'Введите ваш номер'
        }),
        }
