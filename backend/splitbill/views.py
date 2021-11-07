from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from splitbill.models.transaction import Transaction
from splitbill.models.usergroup import UserGroup
from splitbill.serializers.transaction import TransactionSerializer
from splitbill.serializers.usergroup import UserGroupSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    List all user groups, or create a new group.
    """

    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """
    List all transactions, or create a new transaction.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)
