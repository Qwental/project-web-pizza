from users.models import User
from orders.models import Order

def show_notification(user: User):
    notifications = []
    orders = Order.objects.filter(user=user)
    for order in orders:
        if order.get_status_display() == 'Оплачен':
            notifications.append(f'Заказ №{order.pk} оплачен')
        elif order.get_status_display() == 'В пути':
            notifications.append(f'Заказ №{order.pk} в пути')
        elif order.get_status_display() == 'Ожидает':
            notifications.append(f'Заказ №{order.pk} ожидает')
    
    return notifications