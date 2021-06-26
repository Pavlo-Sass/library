from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddForm
from .models import Order


menu = [1, 2, 3]

BASE_CONREXT = {'menu': menu}

def index(request):
    list_orders = list(Order.get_all())
    context = {
        'list_orders': list_orders,
        'title': 'Наші замовлення'
               }
    context.update(BASE_CONREXT)
    return render(request, 'order/index.html', context)

def create_order(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                if not Order.create(**form.cleaned_data):
                    form.add_error(None, f"Шановний_а {form.cleaned_data['user']} На жаль в бібліотеці залишилася тільки одна книжка. І вона конче потрібна бібліотекарю. Спробуйте вибрати іншу книгу")
                else:
                    return redirect('orders')
            except:
                form.add_error(None, 'При додавані замовлення виникла помилка')
    else:
        form = AddForm()
    context = {
        'title': "Створюємо нове замовлення",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/addorder.html', context)

def get_order(request, order_id):
    info = Order.get_by_id(order_id)
    context = {
        'title': f"Замовлення {info.id} ",
        'info': info
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/user.html', context)

def update_order(request, order_id):
    order = Order.get_by_id(order_id)
    order_dict = Order.to_dict(order)
    form = AddForm(order_dict)
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                order.update(**form.cleaned_data)
                return redirect('orders')
            except:
                form.add_error(None, 'При редагувані замовлення виникла помилка')

    context = {
        'order_id': order_id,
        'title': "Редагуємо замовлення",
        'form': form
    }
    context.update(BASE_CONREXT)
    return render(request, 'order/update_order.html', context)

def delete_order(request, order_id):
    if Order.delete_by_id(order_id):
        return redirect('orders')
    return HttpResponse('Памілка!!! Ти намагаєшся видалити не завершене замовлення. Спочатку зазнач дату повернення а потім вже видаляй')