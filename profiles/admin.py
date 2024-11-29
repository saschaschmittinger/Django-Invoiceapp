from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin
from .models import Profile


class ProfileRecources(resources.ModelResource):
    class Meta:
        model = Profile
        fields = {"id", "user"}


@admin.register(Profile)
class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProfileRecources
    list_display = ["firmen_name", "erstellt", "update"]
