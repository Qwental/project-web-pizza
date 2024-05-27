from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm
from users.models import User

from main.models import *


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
            "favorite_products",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # выбор оплаты при регистрации
    cash_payment = forms.ChoiceField(
        choices=[
            ("0", False),  # безнал
            ("1", True),  # налик
        ], required=True, widget=forms.RadioSelect()
    )

    try:
        favorite_products = forms.CheckboxSelectMultiple(choices=[(str(x.id, x) for x in Products.objects.all())])
    except Exception as e:
        print(str(e))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "favorite_products",
        ]


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "cash_payment",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    # выбор оплаты
    cash_payment = forms.ChoiceField(
        choices=[
            ("0", False),  # безнал
            ("1", True),  # налик
        ], required=True, widget=forms.RadioSelect()
    )

    try:
        favorite_products = forms.ModelMultipleChoiceField(queryset=Products.objects.all(), required=False)
    except Exception as e:
        print(str(e))


class ProfileUpdateForm(forms.ModelForm):
    pass
