from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Invoice
from profiles.models import Profile
from .forms import InvoiceForm
from django.views import generic


class Home_base_view(generic.ListView):
    title: str = "SSC Consult"
    template_name: str = "invoices/index.html"
    model = Invoice
    context_object_name: str = "qs"

    def get_queryset(self):
        profil = get_object_or_404(Profile, user=self.request.user)
        return super().get_queryset().filter(profil=profil).order_by("-erstellt")

    def get_context_data(self, **kwargs):
        context = super(Home_base_view, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class InvoiceFormView(generic.FormView):
    title: str = "SSC Create Invoice"
    form_class = InvoiceForm
    template_name: str = "invoices/create.html"
    success_url = reverse_lazy("invoices:base_view")

    def form_valid(self, form):
        profil = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profil = profil
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(InvoiceFormView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)
