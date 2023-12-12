from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from app.views import FavotiteCityViewSet

from usuario.views import login, register

router = DefaultRouter()
router.register(r"favoriteCities", FavotiteCityViewSet)

urlpatterns = [
    path("api/", include(usuario_router.urls)),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/login/", login),
    path("api/register/", register),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
