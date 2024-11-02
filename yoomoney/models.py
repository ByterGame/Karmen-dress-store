from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class BalanceChange(models.Model):
    user_id = models.IntegerField()
    amount_value = models.DecimalField(decimal_places=2, max_digits=99)
    date = models.DateTimeField(_("payment's date"), default=timezone.now)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        status = 'Accepted' if self.is_accepted else 'Declined'
        return (f'Оплата от: {self.date.date()} {self.date.time().hour}:{self.date.time().minute} UTC '
                f'на сумму: {self.amount_value} RUB | Статус: {status} | id пользователя: {self.user_id}.')

