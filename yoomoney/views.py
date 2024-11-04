import json
from django.http import HttpResponseRedirect
from yoomoney.payment import create_payment, payment_acceptance


def create_payment_view(request, total, str_dresses):

    data = {
        'user_id' : request.user.id,
        'total' : total,
        'str_dresses' : str_dresses,
    }
    confirmation_url = create_payment(data)
    return HttpResponseRedirect(confirmation_url)

def create_payment_acceptance(request):
    response = json.loads(request.body)
    payment_acceptance(response)
