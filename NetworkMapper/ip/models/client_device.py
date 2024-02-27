from django.db import models

from NetworkMapper.ip.models import VLAN, WifiNetwork

class ClientDevice(models.Model):
    CONNECTION_TYPES = (
        ("ethernet", "Ethernet"),
        ("wifi", "WiFi"),
    )

    name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True, unique=True)
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE)
    wifi = models.ForeignKey(WifiNetwork, on_delete=models.CASCADE, blank=True, null=True)
    connection_type = models.CharField(max_length=10, choices=CONNECTION_TYPES)

    def __str__(self):
        return self.name
