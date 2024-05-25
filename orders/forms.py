import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
   # phone_number = forms.CharField()
   # email = forms.EmailField()


    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )

    delivery_address = forms.CharField(required=False)

