from enum import Enum

from django.db import models

from common.utils.units import mm_to_inch
from network.models import NetworkDevice

RACK_UNIT_HEIGHT = 44.45  # 1U = 44.45mm


class RackWidth(int, Enum):
    WIDTH_10 = 10
    WIDTH_19 = 19
    WIDTH_23 = 23

    @property
    def width(self) -> float:
        """Width of the Rack in Inches"""
        return self.value

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        """Choices for the Rack Width"""
        return [(width.value, width.name) for width in cls]


class Rack(models.Model):
    name = models.CharField(max_length=50)
    width = models.PositiveIntegerField(choices=RackWidth.choices())
    rack_units = models.FloatField()

    @property
    def height(self) -> float:
        """Total Unit height of the Rack in mm"""
        return round(self.rack_units * RACK_UNIT_HEIGHT)

    @property
    def height_inches(self) -> float:
        """Height of the Rack Item in Inches"""
        return round(mm_to_inch(self.height), 2)

    @property
    def remaining_units(self) -> int:
        """Remaining Rack Units in the Rack"""
        used_units = sum(item.rack_units for item in self.rack_items.all())
        return self.rack_units - used_units


class RackItem(models.Model):
    name = models.CharField(max_length=50)
    rack_units = models.FloatField()
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, related_name="rack_items")
    device = models.OneToOneField(NetworkDevice, on_delete=models.CASCADE, blank=True, null=True, related_name="rack_item")

    @property
    def height(self) -> float:
        """Height of the Rack Item in mm"""
        return round(self.height_units * RACK_UNIT_HEIGHT)

    @property
    def height_inches(self) -> float:
        """Height of the Rack Item in Inches"""
        return round(mm_to_inch(self.height), 2)

    def save(self, *args, **kwargs):
        if self.rack_units > self.rack.remaining_units:
            raise ValueError(f"Not enough space in Rack {self.rack.name} for this RackItem {self.name}")
        super().save(*args, **kwargs)
