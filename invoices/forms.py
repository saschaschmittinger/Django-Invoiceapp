from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    erfüllungsdatum = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    rechnungsdatum = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    zahlungsziel = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Invoice
        fields = (
            "empfänger",
            "rechnungsnummer",
            "erfüllungsdatum",
            "rechnungsdatum",
            "zahlungsziel",
        )
