from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            transport = 'Поездом'
            total_mass = cart.get_total_price()
            if total_mass > 150:
                transport = 'Шаром'
            else:
                transport = 'Поездом'
            cart.clear()
            #запустить асинхронное задание
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'transport': transport, 'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})