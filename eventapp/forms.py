from django import forms

from django.contrib.auth.forms import UserCreationForm

from eventapp.models import User

class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class":"form-control mb-3"}),
            "phone":forms.NumberInput(attrs={"class":"form-control mb-3"}),
        }

class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class EventForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

    date=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    time=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    

