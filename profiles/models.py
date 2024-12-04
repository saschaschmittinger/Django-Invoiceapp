from django.db import models
from django.contrib.auth.models import User

from profiles.utils import generate_konto_nummer


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kontonummer = models.CharField(max_length=26, blank=True)
    firmen_name = models.CharField(max_length=250)
    firmen_info = models.TextField()
    erstellt = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(default="images/avatar.png")
    firmen_logo = models.ImageField(default="images/no_photo.png")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.kontonummer == "":
            self.kontonummer = generate_konto_nummer()
        super().save(*args, **kwargs)


#    def clean(self):
#       if len(self.kontonummer) != 26:
#          raise ValidationError("die Kontonummer muss 26 Stellen haben")
