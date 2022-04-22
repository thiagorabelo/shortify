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

from django.urls import path

from . import views


app_name = "short"

urlpatterns = [
    path("s/<str:uri_hash>/", views.ShortURIRedirectView.as_view(), name="redirect"),

    path("", views.IndexView.as_view(), name="index"),
    path("list/", views.ShortURIListView.as_view(), name="list"),
    path("create/", views.ShortURICreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.ShortURIDeleteView.as_view(), name="delete"),
]
