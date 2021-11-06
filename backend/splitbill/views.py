from django.shortcuts import render
from rest_framework import generics, viewsets

from splitbill.models.usergroup import UserGroup
from splitbill.serializers.usergroup import UserGroupSerializer

# Create your views here.


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    List all user groups, or create a new group.
    """

    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
