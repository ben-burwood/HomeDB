from common.utils.config import get_config_value
from django.db import models


class Circuit(models.Model):
    BREAKER_TYPES = (
        ("fuse", "Fuse"),  # Fuse
        ("mcb", "MCB"),  # Miniature Circuit Breaker
        ("rcd", "RCD"),  # Residual Current Device
        {"rcbo", "RCBO"},  # Residual Current Breaker with Overload
        ("gfci", "GFCI"),  # Ground Fault Circuit Interrupter
    )

    CIRCUIT_TYPES = (
        ("lighting", "Lighting"),
        ("outlet", "Outlets"),
        ("appliance", "Appliance"),
        ("heating", "Heating"),
        ("cooling", "Cooling"),
    )

    name = models.CharField(max_length=100)
    current_rating = models.PositiveIntegerField()
    breaker_type = models.CharField(max_length=10, choices=BREAKER_TYPES)
    spd_protection = models.BooleanField()  # Surge Protection Device
    wire_diameter = models.FloatField()
    circuit_type = models.CharField(max_length=20, choices=CIRCUIT_TYPES)
    description = models.TextField(blank=True)

    @property
    def power_rating(self) -> float:
        return self.current_rating * get_config_value("voltage", 0)

    def __str__(self):
        return self.name
