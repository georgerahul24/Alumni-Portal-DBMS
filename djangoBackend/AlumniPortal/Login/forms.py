from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)
