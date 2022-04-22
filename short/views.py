from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, CreateView, RedirectView, \
    TemplateView, DeleteView

from django.http import HttpRequest

from .models import ShortURI
from .forms import ShortURICreateForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "short/index_view.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("short:list")
        return super().get(request, *args, **kwargs)


class ShortURIListView(LoginRequiredMixin, ListView):
    model = ShortURI
    template_name = "short/shorturi_listview.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ShortURICreateView(LoginRequiredMixin, CreateView):
    model = ShortURI
    form_class = ShortURICreateForm
    template_name = "short/shorturi_createview.html"
    success_url = reverse_lazy("short:list")
    
    def get_form_kwargs(self):
        if self.request.method == "POST":
            self.object = ShortURI(user=self.request.user)
        return super().get_form_kwargs()


class ShortURIDeleteView(LoginRequiredMixin, DeleteView):
    model = ShortURI
    success_url = reverse_lazy("short:list")


class ShortURIRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        try:
            short = ShortURI.objects.get(uri_hash=kwargs['uri_hash'])
            return short.full_uri
        except ShortURI.DoesNotExist:
            return None
