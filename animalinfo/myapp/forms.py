from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'species',
            'habitat',
            'diet',
            'avg_lifespan',
            'image',
        ]
