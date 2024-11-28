from django.contrib import admin
from .models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display: list = ["rechnung", "leistung", "betrag", "erstellt"]
    list_filter: list = ["rechnung", "erstellt"]
    fields: list = ["rechnung", "leistung", "beschreibung", "betrag", "erstellt"]
    readonly_fields: list = ["erstellt"]
