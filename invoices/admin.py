from django.contrib import admin
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display: list = [
        "empfänger",
        "rechnungsnummer",
        "zahlungsziel",
        "abgeschlossen",
    ]
    fields: list = [
        "profil",
        "empfänger",
        "rechnungsnummer",
        "erfüllungsdatum",
        "rechnungsdatum",
        "zahlungsziel",
        "erstellt",
        "abgeschlossen",
    ]
    readonly_fields: list = ["erstellt"]
