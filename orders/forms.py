import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
   # phone_number = forms.CharField()
    email = forms.EmailField()

    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )

    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )

    delivery_address = forms.CharField(required=False)

    #  Пока хз что это
    # def clean_phone_number(self):
    #     data = self.cleaned_data['phone_number']
    #
    #     if not data.isdigit():
    #         raise forms.ValidationError("Номер телефона должен содержать только цифры")
    #
    #     pattern = re.compile(r'^\d{10}$')
    #     if not pattern.match(data):
    #         raise forms.ValidationError("Неверный формат номера")
    #
    #     return data