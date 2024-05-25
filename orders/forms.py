import re
from datetime import datetime, timedelta

# import datetime

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

    def clean_my_time(self):
        start = (datetime.now() + timedelta(minutes=40)).time()
        end = start.replace(hour=23, minute=0, second=0)
        time_pickup_delivery = self.cleaned_data['time_pickup_delivery']
        if (time_pickup_delivery <= start) or (time_pickup_delivery >= end):
            time_pickup_delivery = time_pickup_delivery.strftime("%H:%M")
            start = start.strftime("%H:%M")
            end = end.strftime("%H:%M")
            raise forms.ValidationError(
                f'Выбранное вами время {time_pickup_delivery} не попадает в рабочее время Пиццерии, выберете между {start} и {end}')

        return time_pickup_delivery
