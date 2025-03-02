from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=250, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class AddDentist(UserCreationForm):
    dentist = forms.ChoiceField(
        required=True, choices=(("dentist", "Dentist"), ("user", "User"))
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "dentist")
