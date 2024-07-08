from django import forms

from network.models import VLAN, WifiNetwork
from network.models.ip import IpRange

class IpRangeForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea(attrs={"style": "height:50px;"}), required=False)

    class Meta:
        model = IpRange
        fields = ["start_address", "end_address", "num_addresses", "description"]

class VLANForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"style": "height:50px;"}), required=False)

    class Meta:
        model = VLAN
        fields = ["vlan_id", "name", "description"]

class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiNetwork
        fields = ["ssid", "password"]
