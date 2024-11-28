from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_nummer = models.CharField(max_length=26, blank=True)
    firmen_name = models.CharField(max_length=250)
    firmen_info = models.TextField()
    erstellt = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
