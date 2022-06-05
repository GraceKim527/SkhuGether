from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_id', 'user_phonenum', 'feedback_content']

        widgets = {
            'user_id': forms.TextInput(attrs={'placeholder': 'Name'}),
            'user_phonenum': forms.TextInput(attrs={'placeholder': 'PhoneNumber'}),
            'feedback_content': forms.Textarea(attrs={'placeholder': 'Feedback Here'}),
        } 