from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if '@' not in email:
            raise ValidationError('Enter a valid email address.')
        elif User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')

        return email
