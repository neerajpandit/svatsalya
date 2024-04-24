from django import forms




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)





class ImageForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()