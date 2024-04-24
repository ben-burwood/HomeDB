import re

from django.core.exceptions import ValidationError
from django.db import models

from .vlan import VLAN
from .wifi import WifiNetwork


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

    def clean(self):
        super().clean()

        if not self.mac_address_validation(self.mac_address):
            raise ValidationError("Invalid MAC Address format")

    @staticmethod
    def mac_address_validation(mac_address: str) -> bool:
        MAC_ADDRESS_PATTERN = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})$"
        return re.match(MAC_ADDRESS_PATTERN, mac_address) is not None
