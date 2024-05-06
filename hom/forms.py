from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
       
    email = forms.EmailField(widget=forms.EmailInput)

    password1 = forms.CharField(widget=forms.PasswordInput)
   
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)

    password = forms.CharField(widget=forms.PasswordInput)



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'gender', 'birthdate','image']

