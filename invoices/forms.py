from django.forms import *
from .models import Invoice



class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = (
            "empfänger",
            "rechnungsnummer",
            "erfüllungsdatum",
            "rechnungsdatum",
            "zahlungsziel",
        )
