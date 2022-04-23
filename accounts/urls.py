from django.contrib import admin
from django.contrib.auth.views import \
     PasswordResetView, PasswordResetDoneView, \
     PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views


app_name = "accounts"

urlpatterns = [
     path("signup/", views.SignUpView.as_view(), name="signup"),

     # Password reset

     path("password_reset/",
          PasswordResetView.as_view(template_name="accounts/password_reset_form.html",
                                    email_template_name="accounts/email/password_reset_email.txt",
                                    html_email_template_name="accounts/email/password_reset_email.html",
                                    success_url=reverse_lazy("accounts:password_reset_done")),
          name="password_reset"),
     
     path("password_reset_done/",
          PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
          name="password_reset_done"),

     path("password_reset_confirm/<str:uidb64>/<str:token>/",
          PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm_form.html",
                                           success_url=reverse_lazy("accounts:password_reset_complete")),
          name="password_reset_confirm"),
     
     path("password_reset_complete/",
          PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
          name="password_reset_complete"),
]
