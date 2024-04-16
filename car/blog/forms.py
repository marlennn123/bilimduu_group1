from django import forms
from allauth.account.forms import SignupForm


class CustomSignUpForm(SignupForm):
    age = forms.IntegerField(label='Возраст', required=False)
