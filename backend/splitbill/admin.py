from django.contrib import admin

from splitbill.models.transaction import Transaction
from splitbill.models.usergroup import UserGroup
from splitbill.models.userbalance import UserBalance

admin.site.register(Transaction)
admin.site.register(UserGroup)
admin.site.register(UserBalance)
