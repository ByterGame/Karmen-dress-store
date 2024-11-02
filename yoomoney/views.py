import json
from django.http import HttpResponseRedirect
from yoomoney.payment import create_payment


def create_payment_view(request):
    confirmation_url = create_payment(request.user.id)
    return HttpResponseRedirect(confirmation_url)

# def create_payment_acceptance(request): вьюшка для обработки результата оплаты
#     response = json.loads(request.body)
#     payment_acceptance(response)
