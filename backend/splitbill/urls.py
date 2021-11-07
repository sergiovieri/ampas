from django.urls import include, path
from rest_framework.routers import DefaultRouter

from splitbill import views

router = DefaultRouter()
router.register(r"usergroups", views.UserGroupViewSet)
router.register(r"transactions", views.TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
