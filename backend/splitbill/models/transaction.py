from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        GENERAL = "GEN", _("General")

    created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    # Group ID == 0 means non-group transaction
    group_id = models.PositiveIntegerField()
    owner_id = models.PositiveIntegerField()

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, blank=True, default="")
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency="USD")
    type = models.CharField(
        max_length=3,
        choices=TransactionType.choices,
        default=TransactionType.GENERAL,
    )

    class Meta:
        ordering = ["-created"]
