from django.db import models
from invoices.models import Invoice


class Position(models.Model):
    rechnung = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    leistung = models.CharField(max_length=200)
    beschreibung = models.TextField(blank=True, help_text="Optionale Info")
    betrag = models.FloatField(help_text="in EUR €")
    erstellt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rechnung: {self.rechnung.rechnungsnummer}"
