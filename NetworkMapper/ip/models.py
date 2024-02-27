from django.db import models


class VLAN(models.Model):
    vlan_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vlan_id} - {self.name}"

    @property
    def subnet(self) -> str:
        return f"192.168.{self.vlan_id}.0/24"


class WifiNetwork(models.Model):
    ssid = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ssid
