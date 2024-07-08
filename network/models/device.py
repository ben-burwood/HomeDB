import re

from django.core.exceptions import ValidationError
from django.db import models

from network.models.vlan import VLAN
from network.models.wifi import WifiNetwork
from network.objects import ConnectionType, InfrastructureDeviceType, NetworkDeviceType

class Device(models.Model):
    """Generic Device with a Name"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class NetworkedDevice(Device):
    """Networked Device with MAC Address, IP Address, VLAN, and Connection Type (and/or WiFi Network)"""

    mac_address = models.CharField(max_length=17, unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True, unique=True)
    vlan = models.ForeignKey(VLAN, on_delete=models.CASCADE, blank=True, null=True)
    wifi = models.ForeignKey(WifiNetwork, on_delete=models.CASCADE, blank=True, null=True)
    connection_type = models.CharField(max_length=10, choices=ConnectionType.choices())

    def clean(self):
        super().clean()

        if not self.mac_address_validation(self.mac_address):
            raise ValidationError("Invalid MAC Address format")

    @staticmethod
    def mac_address_validation(mac_address: str) -> bool:
        MAC_ADDRESS_PATTERN = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})$"
        return re.match(MAC_ADDRESS_PATTERN, mac_address) is not None

    class Meta:
        abstract = True


class ClientDevice(NetworkedDevice):
    pass


class NetworkDevice(NetworkedDevice):
    device_type = models.CharField(max_length=20, choices=NetworkDeviceType.choices())


class InfrastructureDevice(Device):
    device_type = models.CharField(max_length=20, choices=InfrastructureDeviceType.choices())
