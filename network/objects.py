from enum import Enum


class ConnectionType(Enum):
    ETHERNET = "ethernet"
    WIFI = "wifi"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Choices for the Connection Types"""
        return [(connection.name, connection.value.capitalize()) for connection in cls]


class NetworkDeviceType(Enum):
    ROUTER = "router"
    FIREWALL = "firewall"
    SWITCH = "switch"
    ACCESS_POINT = "access_point"
    STORAGE = "storage"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Choices for the Network Device Types"""
        return [(device.name, device.value.capitalize()) for device in cls]


class InfrastructureDeviceType(Enum):
    POWER = "power"
    PATCH_PANEL = "patch_panel"
    BLANK = "blank"
    CABLE_MANAGEMENT = "cable_management"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Choices for the Infrastructure Device Types"""
        return [(device.name, device.value.capitalize()) for device in cls]
