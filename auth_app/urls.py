from django.urls import path
from .views import RegisterView, RefreshTokenView
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]