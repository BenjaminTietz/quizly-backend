from django.urls import path
from .views import RegisterView
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]