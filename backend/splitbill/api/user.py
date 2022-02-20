from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from splitbill.models.user import User
from splitbill.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    List all user, or create a new group.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]