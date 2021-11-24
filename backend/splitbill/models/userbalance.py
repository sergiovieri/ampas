from django.db import models
from djmoney.models.fields import MoneyField


class UserBalance(models.Model):
    # Group ID == 0 means non-group transaction
    group_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    balance = MoneyField(max_digits=19, decimal_places=4, default_currency="USD")

    class Meta:
        unique_together = (("group_id", "user_id"),)
        indexes = [
            models.Index(fields=["group_id", "user_id"]),
        ]
