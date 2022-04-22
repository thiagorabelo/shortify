from django.contrib import admin
from django.urls import path, include, reverse_lazy

from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
