from django.urls import include, path
from rest_framework.routers import DefaultRouter

from splitbill import viewsets

router = DefaultRouter()
router.register(r"usergroups", viewsets.UserGroupViewSet)
router.register(r"transactions", viewsets.TransactionViewSet)
router.register(r"userbalances", viewsets.UserBalanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
