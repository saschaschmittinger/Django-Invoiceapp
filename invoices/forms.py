from django import forms
from django.forms import ValidationError

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    erfüllungsdatum = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Erfüllungsdatum"
    )
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["erfüllungsdatum"].label = (
            "<span class='label-erfüllungsdatum'>Erfüllungsdatum</span>"
        )
        self.fields["rechnungsdatum"].label = (
            "<span class='label-erfüllungsdatum'>Rechnungsdatum</span>"
        )
        self.fields["zahlungsziel"].label = (
            "<span class='label-erfüllungsdatum'>Zahlungsziel</span>"
        )
        self.fields["empfänger"].label = (
            "<span class='label-erfüllungsdatum'>Empfänger</span>"
        )
        self.fields["rechnungsnummer"].label = (
            "<span class='label-erfüllungsdatum'>Rechnungsnummer</span>"
        )

    def clean_rechnungsnummer(self):
        rechnungsnr = self.cleaned_data.get("rechnungsnummer")
        if len(rechnungsnr) < 10:
            raise ValidationError("Rechnungsnummer ist zu kurz")
        return rechnungsnr
