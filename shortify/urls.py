"""shortify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from accounts.views import LogoutView, LoginView


urlpatterns = [
    path("", include("short.urls", namespace="short")),

    path("logout/", LogoutView.as_view(next_page=reverse_lazy("login")), name="logout"),
    path("login/", LoginView.as_view(template_name="accounts/login_view.html"), name="login"),

    path("accounts/", include("accounts.urls", namespace="accounts")),

    path("admin/", admin.site.urls),
]
