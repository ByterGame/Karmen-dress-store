from importlib.metadata import metadata
from yoomoney.models import BalanceChange
from yookassa import Configuration, Payment

Configuration.account_id = 484924
Configuration.secret_key = 'test_XtVlzBPW40VDbdG6kogjB43VgTk0XzGmoCSHGHmldZM'

def create_payment(data):

    change = BalanceChange.objects.create(
        user_id=data['user_id'],
        amount_value=300,
        is_accepted=True, #так как результат платежа не обрабатывается на локал хосте, то по дефолту ставим True
    )

    payment = Payment.create({
        'amount': {
            'value': data['total'],
            'currency': 'RUB',
        },
        'payment_method_data': {
            'type': 'bank_card',
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://example.com',
        },
        'metadata': {
            'table_id': change.id,
            'user_id': data['user_id'],
        },
        'capture': True,
        'refundable': False,
        'description': 'Оплата на сумму ' + str(data['total']),
    })


    return payment.confirmation.confirmation_url


# def payment_acceptance(response): функция для обработки результата оплаты
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
#     elif response['event'] == 'payment.canceled':
#         table.is_accepted = False
#     return True