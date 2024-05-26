from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

    username = forms.CharField(label="Ник", widget=forms.TextInput(attrs={'class': 'form-control-username'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control-pass'}))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "cash_payment",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # выбор типа оплаты при регистрации
    cash_payment = forms.ChoiceField(
        choices=[
            ("0", False),  # безнал
            ("1", True),  # налик
        ], required=True, widget=forms.RadioSelect()
    )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

class ProfileUpdateForm(forms.ModelForm):
    pass
