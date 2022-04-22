from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView  # Do not delete me.
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreationForm

# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup_view.html"
    success_message = "Your account was created successfully"
