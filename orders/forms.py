import re
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError

# import datetime
from orders.models import Order
from django import forms






# Та самая нагруженность
def current_service_load():
    flag_load = False
    orders = Order.objects.all()
    # Создаем словарь, где ключ - интервал, значение - текущая нагруженность на интервал

    start_time = (datetime.now()).replace(hour=9, minute=0)
    intervals_load = {}
    for i in range(28):
        s = f'{start_time.strftime("%H:%M")}-'
        start_time = (start_time + timedelta(minutes=30))
        s += f'{start_time.strftime("%H:%M")}'
        intervals_load[s] = 0
        s = ''

    for order in orders:
        if order.get_status_display() != 'Получен':
            time_order = order.time_pickup_delivery
            #print(time_order)

            for key in intervals_load.keys():
                start_interval = datetime.strptime((str(str(key).split('-')[0])), "%H:%M").time()
                end_interval = datetime.strptime((str(str(key).split('-')[1])), "%H:%M").time()
                #print(start_interval, time_order, end_interval)
                if (start_interval<=time_order <=end_interval):
                    intervals_load[key] += 1
                    if intervals_load[key] > 4:
                        flag_load = True
                    break

        if flag_load:
            break

    return flag_load


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # phone_number = forms.CharField()

    time_pickup_delivery = forms.TimeField()
    email = forms.EmailField()
    delivery_address = forms.CharField(required=False)

    # Валидация времени
    def clean_my_time(self, requires_delivery):

        print('requires_delivery', requires_delivery)
        time_pickup_delivery = self.cleaned_data['time_pickup_delivery']
        flag_working_time = True

        if requires_delivery == 1:
            # Доставка
            # + 30 минут только из-за доставки
            start = (datetime.now() + timedelta(minutes=30)).time()
            end = start.replace(hour=23, minute=30, second=0)
        elif requires_delivery == 0:
            # Самовывоз
            # + 10 минут только из-за НАЧАЛА ГОТОВКИ И ОБРАБОТКИ
            start = (datetime.now() + timedelta(minutes=10)).time()
            end = start.replace(hour=22, minute=50, second=0)
        else:
            raise forms.ValidationError(
                f'Ни Самовывоз, Ни Доставка. Кто ты воин?')
        flag_working_time = False
        if start > end:
            flag_pizza_close = True

        #Проверка времени на попадания в часы работы
        if (time_pickup_delivery <= start.replace(hour=9, minute=0, second=0)) or (time_pickup_delivery >= end):
            # Время невалидное, т.е. не попадает в рабочий интервал
            flag_working_time = True
        flag_current_service_load = current_service_load()

        if flag_working_time:
            time_pickup_delivery = time_pickup_delivery.strftime("%H:%M")
            raise ValidationError(
                f'Выбранное вами время {time_pickup_delivery} не попадает в рабочее время '
                f'Пиццерии. Рабочее время с 9:00 до 23:00')

        elif flag_working_time: #если  flag_working_time == False
            time_pickup_delivery = time_pickup_delivery.strftime("%H:%M")
            start = start.strftime("%H:%M")
            end = end.strftime("%H:%M")
            raise forms.ValidationError(
                f'Выбранное вами время {time_pickup_delivery} не попадает в рабочее время '
                f'Пиццерии, выберете между {start} и {end}')
        elif flag_current_service_load:
            print('В данный момент сервис перегружен{current_service_statuses}')
            # Добавляем к start еще 10 минут ввиду загрузки кухни
            start = (datetime.now() + timedelta(minutes=10)).time()
            if (time_pickup_delivery <= start) or (time_pickup_delivery >= end):
                time_pickup_delivery = time_pickup_delivery.strftime("%H:%M")
                start = start.strftime("%H:%M")
                end = end.strftime("%H:%M")
                raise forms.ValidationError(
                    f'В данный момент сервис перегружен заказами и выбранное вами время {time_pickup_delivery} '
                    f'не попадает в доступные время '
                    f'Пиццерии, выберете между {start} и {end}')
        return time_pickup_delivery
