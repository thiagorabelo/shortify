from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import path, include, reverse_lazy

from . import views


app_name = "accounts"

urlpatterns = [
     path("signup/", views.SignUpView.as_view(), name="signup"),

     # Password reset
     path("change_password/",
          PasswordResetView.as_view(template_name="accounts/password_reset_form.html",
                                    email_template_name="accounts/email/password_reset_email.txt",
                                    html_email_template_name="accounts/email/password_reset_email.html",
                                    success_url=reverse_lazy("short:index")),
          name="password_reset"),

     # TODO: Incomplete
     path("confirm_password/<str:uidb64>/<str:token>/",
          PasswordResetConfirmView.as_view(),
          name="password_confirm")
]
