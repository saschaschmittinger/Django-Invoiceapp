from django import forms
from .models import Position


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ("leistung", "beschreibung", "betrag")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["leistung"].label = (
            "<span class='label-erfüllungsdatum'>Leistung</span>"
        )
        self.fields["beschreibung"].label = (
            "<span class='label-erfüllungsdatum'>Beschreibung</span>"
        )
        self.fields["betrag"].label = (
            "<span class='label-erfüllungsdatum'>Betrag</span>"
        )
