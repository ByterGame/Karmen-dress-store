import json
from django.http import HttpResponseRedirect
from yoomoney.payment import create_payment


def create_payment_view(request, total):
    data = {
        'user_id' : request.user.id,
        'total' : total,
    }
    confirmation_url = create_payment(data)
    return HttpResponseRedirect(confirmation_url)

# def create_payment_acceptance(request): вьюшка для обработки результата оплаты
#     response = json.loads(request.body)
#     payment_acceptance(response)
