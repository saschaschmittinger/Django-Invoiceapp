from django.db import models
from profiles.models import Profile
from receivers.models import Receiver


class Invoice(models.Model):
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    empfänger = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    rechnungsnummer = models.CharField(max_length=150)
    erfüllungsdatum = models.DateField()
    rechnungsdatum = models.DateField()
    zahlungsziel = models.DateField()
    erstellt = models.DateTimeField(auto_now_add=True)
    abgeschlossen = models.BooleanField(default=False)

    def __str__(self):
        return f"Rechnungsnummer: {self.rechnungsnummer}, pk: {self.pk}"

    def get_positions(self):
        pass

    def get_total_amount(self):
        pass
