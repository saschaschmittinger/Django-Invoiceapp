from django.contrib import admin
from .models import Invoice, Tag
from import_export import resources
from import_export.admin import ExportActionMixin


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields: dict = {"id", "name"}


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
        "tags",
    ]
    readonly_fields: list = ["erstellt"]


@admin.register(Tag)
class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource
    fields: list = ["name"]
