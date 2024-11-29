from django.db import models
from profiles.models import Profile
from receivers.models import Receiver


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    empfänger = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    rechnungsnummer = models.CharField(max_length=150)
    erfüllungsdatum = models.DateField()
    rechnungsdatum = models.DateField()
    zahlungsziel = models.DateField()
    erstellt = models.DateTimeField(auto_now_add=True)
    abgeschlossen = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Rechnungsnummer: {self.rechnungsnummer}"

    @property
    def tags(self):
        return self.tags.all()

    @property
    def positions(self):
        return self.position_set.all()

    @property
    def total_amount(self):
        total = 0
        qs = self.positions
        for pos in qs:
            total += pos.betrag
        return total
