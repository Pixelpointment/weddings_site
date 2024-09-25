from django import forms
from .models import GuestPhoto, Colours

class GuestPhotoForm(forms.ModelForm):
    class Meta:
        model = GuestPhoto
        fields = ['uploader_name', 'photo', 'description']
        widgets = {
            'uploader_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Optional description'}),
        }

class ColoursForm(forms.ModelForm):
    class Meta:
        model = Colours
        fields = ['primary_color', 'secondary_color', 'accent_color', 'font_color', 'btn_hover_color']
        widgets = {
            'primary_color': forms.TextInput(attrs={'type': 'color'}),
            'secondary_color': forms.TextInput(attrs={'type': 'color'}),
            'accent_color': forms.TextInput(attrs={'type': 'color'}),
            'font_color': forms.TextInput(attrs={'type': 'color'}),
            'btn_hover_color': forms.TextInput(attrs={'type': 'color'}),
        }
