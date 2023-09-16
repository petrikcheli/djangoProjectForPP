from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведомления по электронной почте
    при успешном создании заказа
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order.id}'
    message = f'Дорогой {order.first_name},\n\n' \
              f'Вы успешно разместили заказ.' \
              f'Ваш идентификатор заказа: {order.id}.'
    mail_sent = send_mail(subject, message, 'petricheli@mail.ru', [order.email])
    return mail_sent
