import json
from django.http import HttpResponseRedirect

from users.models import Order
from yoomoney.models import BalanceChange
from yoomoney.payment import create_payment


def create_payment_view(request):
    count = request.GET.get("count", 0)
    sizes = request.GET.get("sizes", 0)
    total = request.GET.get("total", 0)
    str_dresses = request.GET.get("str_dresses", "")
    print(f'count: {count}, sizes: {sizes}')
    data = {
        'user_id': request.user.id,
        'total': total,
        'str_dresses': str_dresses,
    }
    confirmation_url = create_payment(data)
    return HttpResponseRedirect(confirmation_url)

# def create_payment_acceptance(request, id):
#     response = json.loads(request.body)
#     payment_acceptance(response, id)

def payment_accept(request, id):
    payment = BalanceChange.objects.get(id=id)
    payment.is_accepted = True
    order_id = payment.order_id
    order = Order.objects.get(id=order_id)
    order.is_paid = True
    order.save()
    payment.save()
    return HttpResponseRedirect('/')
