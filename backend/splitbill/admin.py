from django.contrib import admin

from splitbill.models.transaction import Transaction
from splitbill.models.usergroup import UserGroup

admin.site.register(Transaction)
admin.site.register(UserGroup)
