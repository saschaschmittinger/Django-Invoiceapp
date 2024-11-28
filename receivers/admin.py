from django.contrib import admin
from .models import Receiver


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    fields: list = ["name", "adresse", "webseite", "erstellt"]
    list_display: list = ["name", "adresse", "erstellt"]
