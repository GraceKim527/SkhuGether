from django import forms
from .models import Lost, Comment

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['title', 'content','classroom', 'image', 'password']

class CheckPasswordForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['password']

class LostEditForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['title', 'content','classroom', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']