from django import forms

from .models import VLAN, WifiNetwork

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ["vlan_id", "name", "description"]


class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiNetwork
        fields = ["ssid", "password"]
