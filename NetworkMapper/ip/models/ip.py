from django.core.exceptions import ValidationError
from django.db import models


class IpRange(models.Model):
    start_address = models.GenericIPAddressField()
    end_address = models.GenericIPAddressField()
    num_addresses = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def clean(self):
        super().clean()

        if self.start_address > self.end_address:
            raise ValidationError("Start Address must be Lower than End Address")

        if self.start_address.protocol != self.end_address.protocol:
            raise ValidationError("Start Address and End Address must be of the same IP Version")

        for other_ip_range in IpRange.objects.exclude(pk=self.pk):
            if self.check_overlap(other_ip_range):
                raise ValidationError("IP Range overlaps with another IP Range : " + other_ip_range)

    def check_overlap(self, other: "IpRange") -> bool:
        """Check if the given IP Range overlaps with the current IP Range"""
        if self.start_address <= other.start_address <= self.end_address:
            return True
        if self.start_address <= other.end_address <= self.end_address:
            return True
        if other.start_address <= self.start_address <= other.end_address:
            return True
        if other.start_address <= self.end_address <= other.end_address:
            return True
        return False

    @staticmethod
    def ipv4_to_numeric(ip):
        octets = ip.split(".")

        for octet in octets:
            if not octet.isdigit() or not 0 <= int(octet) <= 255:
                raise ValueError("Invalid IPv4 address format")

        numeric_ip = 0
        for i in range(4):
            numeric_ip += int(octets[i]) * (256 ** (3 - i))
        return numeric_ip
