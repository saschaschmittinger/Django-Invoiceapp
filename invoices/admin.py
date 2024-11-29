from django.contrib import admin
from import_export import resources
from import_export.fields import Field
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
    profil = Field()
    empfänger = Field()
    erstellt = Field()
    abgeschlossen = Field()
    positions = Field()
    total_amount = Field()

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
            "positions",
            "total_amount",
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
            "positions",
            "total_amount",
        )

    def dehydrate_profil(self, obj):
        return obj.profil.user.username

    def dehydrate_empfänger(self, obj):
        return obj.empfänger.name

    def dehydrate_erstellt(self, obj):
        return obj.erstellt.strftime("%d-%m-%y")

    def dehydrate_abgeschlossen(self, obj):
        if obj.abgeschlossen == True:
            return "Ja"
        else:
            return "Nein"

    def dehydrate_positions(self, obj):
        positions_list = [x.leistung for x in obj.positions]
        positions_str = ", ".join(positions_list)
        return positions_str

    def dehydrate_total_amount(self, obj):
        return obj.total_amount


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
