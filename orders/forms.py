import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # phone_number = forms.CharField()
    #
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    time_pickup_delivery = forms.TimeField()
    email = forms.EmailField()
    delivery_address = forms.CharField(required=False)

