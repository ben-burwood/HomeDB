from django.db import models


VOLTAGE = 240


class Circuit(models.Model):
    BREAKER_TYPES = (
        ("fuse", "Fuse"),
        ("mcb", "MCB"),
        ("rcd", "RCD"),
        ("gfci", "GFCI"),
    )

    CIRCUIT_TYPES = (
        ("lighting", "Lighting"),
        ("outlet", "Outlet"),
        ("appliance", "Appliance"),
        ("heating", "Heating"),
        ("cooling", "Cooling"),
    )

    name = models.CharField(max_length=100)
    current_rating = models.IntegerField()
    breaker_type = models.CharField(max_length=10, choices=BREAKER_TYPES)
    spd_protection = models.BooleanField()  # Surge Protection Device
    wire_diameter = models.FloatField()
    circuit_type = models.CharField(max_length=20, choices=CIRCUIT_TYPES)
    description = models.TextField(blank=True)

    @property
    def power_rating(self) -> float:
        return self.current_rating * VOLTAGE

    def __str__(self):
        return self.name
