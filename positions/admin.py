from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
from .models import Position


class PositionResource(resources.ModelResource):
    erstellt = Field()
    rechnung = Field()
    beschreibung = Field()

    class Meta:
        model = Position
        fields = {"id", "leistung", "rechnung", "beschreibung", "betrag", "erstellt"}

    def dehydrate_rechnung(self, obj):
        return obj.rechnung.rechnungsnummer

    def dehydrate_erstellt(self, obj):
        return obj.erstellt.strftime("%d-%m-%y")

    def dehydrate_beschreibung(self, obj):
        if obj.beschreibung == "":
            return "-"
        return obj.beschreibung


@admin.register(Position)
class PositionAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PositionResource
    list_display: list = ["rechnung", "leistung", "betrag", "erstellt"]
    list_filter: list = ["rechnung", "erstellt"]
