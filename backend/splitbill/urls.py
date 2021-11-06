from django.urls import include, path
from rest_framework.routers import DefaultRouter

from splitbill import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"usergroups", views.UserGroupViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
