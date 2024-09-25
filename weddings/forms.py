from django import forms
from .models import GuestPhoto

class GuestPhotoForm(forms.ModelForm):
    class Meta:
        model = GuestPhoto
        fields = ['photo', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional message...'}),
        }

