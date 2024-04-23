from django import forms
from .models import Image



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
