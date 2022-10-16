from django import forms
from .models import Lost

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['title', 'content','classroom', 'image', 'password']

class LostEditForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['title', 'content','classroom', 'image']