from django.shortcuts import render, get_object_or_404
from invoices.models import Invoice
from profiles.models import Profile
from django.views import generic


class Home_base_view(generic.ListView):
    title: str = "SSC Consult"
    template_name = "invoices/index.html"
    model = Invoice
    context_object_name = "qs"

    def get_queryset(self):
        profil = get_object_or_404(Profile, user=self.request.user)
        return super().get_queryset().filter(profil=profil).order_by("-erstellt")

    def get_context_data(self, **kwargs):
        context = super(Home_base_view, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)
