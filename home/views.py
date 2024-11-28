from django.shortcuts import render
from invoices.models import Invoice
from django.http import HttpResponse


def hello_world(request):
    title: str = "SSC Invoice"
    template: str = "template_name"
    obj = Invoice.objects.get(id=1)
    qs = Invoice.objects.all()
    context: dict = {"title": title}
    return HttpResponse("Hallo Sascha")
