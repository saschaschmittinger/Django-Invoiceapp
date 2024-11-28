from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display: list = ["firmen_name", "user", "erstellt", "update"]
    list_filter: list = ["firmen_name", "erstellt", "user"]
    fields: list = [
        "user",
        "account_nummer",
        "firmen_name",
        "firmen_info",
        "erstellt",
        "update",
    ]
    readonly_fields: list = ["erstellt", "update"]
