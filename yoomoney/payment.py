from importlib.metadata import metadata

from products.models import Dress
from users.models import Order
from yoomoney.models import BalanceChange
from yookassa import Configuration, Payment

Configuration.account_id = 484924
Configuration.secret_key = 'test_XtVlzBPW40VDbdG6kogjB43VgTk0XzGmoCSHGHmldZM'


def create_payment(user_id, order, text='Были куплены: '):
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
        is_accepted=True,
    )
    order.is_paid = True
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
            'return_url': f'https://f507-87-225-75-120.ngrok-free.app/',
        },
        'metadata': {
            'table_id': change.id,
            'user_id': user_id,
        },
        'capture': True,
        'refundable': False,
        'description': 'Оплата на сумму ' + str(order.order_sum),
    })

    return payment.confirmation.confirmation_url


def payment_acceptance(response):
    try:
        table = BalanceChange.objects.get(
            id=response['object']['metadata']['table_id'],
        )
    except BalanceChange.DoesNotExist:
        # payment_id = response['object']['id']
        return False

    if response['event'] == 'payment.succeeded':
        table.is_accepted = True
        table.save()

    elif response['event'] == 'payment.canceled':
        table.is_accepted = False
    return True