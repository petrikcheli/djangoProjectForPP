from django.shortcuts import render
from .forms import OrderCreateForm
from .tasks import order_created


def custom_order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            #запустить асинхронное задание
            #order_created.delay(order.id)
            return render(request,
                          'orderscustoms/ordercustom/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orderscustoms/ordercustom/create.html',
                  {'form': form})