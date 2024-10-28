from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


def check_email_exist(email):
    return False


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'country', 'avatar', 'password1', 'password2')

    def clean_email(self):
        cleaned_data = self.cleaned_data.get('email')

        if check_email_exist(cleaned_data):
            raise forms.ValidationError('Ошибка такая почта уже используется')

        return cleaned_data


class EmailForm(forms.Form):
    email = forms.CharField()
