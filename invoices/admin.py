from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin
from .models import Invoice, Tag


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields: dict = {
            "id",
            "name",
        }


class InvoiceResource(resources.ModelResource):
    class Meta:
        model = Invoice
        fields: dict = {
            "id",
            "profil",
            "empfänger",
            "rechnungsnummer",
            "erfüllungsdatum",
            "rechnungsdatum",
            "zahlungsziel",
            "erstellt",
            "abgeschlossen",
        }
        export_order = (
            "id",
            "profil",
            "empfänger",
            "rechnungsnummer",
            "rechnungsdatum",
            "erfüllungsdatum",
            "erstellt",
            "zahlungsziel",
            "abgeschlossen",
        )


@admin.register(Invoice)
class InvoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = InvoiceResource
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
        "tags",
    ]
    readonly_fields: list = ["erstellt"]


@admin.register(Tag)
class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource
    fields: list = ["name"]
