from django import forms
from .models import Casterm

class CastermForm(forms.ModelForm):
    class Meta:
        model = Casterm
        fields = ['name', 'role', 'gender', 'image']