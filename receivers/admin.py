from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin
from .models import Receiver


class ReceiverResources(resources.ModelResource):
    class Meta:
        model = Receiver
        fields = {"id", "name", "adresse", "webseite", "erstellt"}
        export_order = ("id", "name", "adresse", "webseite", "erstellt")


@admin.register(Receiver)
class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ReceiverResources
    list_display: list = ["name", "adresse", "erstellt"]
