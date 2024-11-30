from django.shortcuts import render
from invoices.models import Invoice
from django.views import generic


class Home_base_view(generic.ListView):
    title: str = "SSC Consult"
    template_name = "base.html"
    queryset = Invoice.objects.all()
    context_object_name = "invoices"

    def get_context_data(self, **kwargs):
        context = super(Home_base_view, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)
