import uuid
from importlib.metadata import metadata

from products.models import Dress
from users.models import Order
from yoomoney.models import BalanceChange
from yookassa import Configuration, Payment

Configuration.account_id = 484924
Configuration.secret_key = 'test_XtVlzBPW40VDbdG6kogjB43VgTk0XzGmoCSHGHmldZM'


def create_payment(user_id, order, text='Были куплены: '):
    idempotency_key = str(uuid.uuid4())
    for item in order.items:
        dress_id = int(item["id"])
        dress = Dress.objects.get(id=dress_id)
        name = dress.name
        text += f"{name}, "

    change = BalanceChange.objects.create(
        user_id=user_id,
        amount_value=order.order_sum,
        purchase=text,
        order=order,
        is_accepted=False,
    )
    order.is_paid = False
    order.save()

    payment = Payment.create({
        'amount': {
            'value': order.order_sum,
            'currency': 'RUB',
        },
        'payment_method_data': {
            'type': 'bank_card',
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': f'https://47e6-62-76-6-79.ngrok-free.app//yoomoney/payment-accept/{change.id}',
        },
        'metadata': {
            'table_id': change.id,
            'user_id': user_id,
        },
        'capture': True,
        'refundable': False,
        'description': 'Оплата на сумму ' + str(order.order_sum),
    },idempotency_key=idempotency_key)

    return payment.confirmation.confirmation_url

#
# def payment_acceptance(response, id):
#     try:
#         table = BalanceChange.objects.get(
#             id=response['object']['metadata']['table_id'],
#         )
#     except BalanceChange.DoesNotExist:
#         # payment_id = response['object']['id']
#         return False
#
#     if response['event'] == 'payment.succeeded':
#         table.is_accepted = True
#         table.save()
#         order_id = table.order_id
#         order = Order.objects.get(id = order_id)
#         order.is_paid = True
#         order.save()
#
#     elif response['event'] == 'payment.canceled':
#         table.is_accepted = False
#     return True