from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
from .models import Profile


class ProfileRecources(resources.ModelResource):
    user = Field()

    class Meta:
        model = Profile
        fields = {
            "id",
            "user",
            "kontonummer",
            "firmen_name",
            "firmen_info",
            "erstellt",
            "update",
        }

    def dehydrate_user(self, obj):
        return obj.user.username


@admin.register(Profile)
class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProfileRecources
    list_display = ["firmen_name", "erstellt", "update"]
