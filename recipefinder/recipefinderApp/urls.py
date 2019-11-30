from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"profiles", views.ProfileViewSet)


urlpatterns = [
    path("hello/", views.HelloView.as_view(), name="hello"),
    path("", include(router.urls)),
    path("", views.IndexView),
]
