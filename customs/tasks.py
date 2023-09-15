from celery import shared_task
from django.core.mail import send_mail
from .models import customs


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведомления по электронной почте
    при успешном создании заказа
    """
    order = customs.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
        f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'petricheli@mail.ru', [order.email])
    return mail_sent