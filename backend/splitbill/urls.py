from django.urls import include, path
from rest_framework.routers import DefaultRouter

from splitbill import viewsets
from splitbill.api import user

router = DefaultRouter()
router.register(r"usergroups", viewsets.UserGroupViewSet)
router.register(r"transactions", viewsets.TransactionViewSet)
router.register(r"userbalances", viewsets.UserBalanceViewSet)
router.register(r"users", user.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
