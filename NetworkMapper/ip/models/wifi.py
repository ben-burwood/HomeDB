from django.db import models


class WifiNetwork(models.Model):
    ssid = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ssid
