from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    remember_me = forms.BooleanField(label='Remember Me', required=False, initial=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username:
            raise Exception('Username', 'cannot be empty')

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise Exception('Password', 'cannot be empty')

        return password

