from django import forms

from .models import ClientDevice, VLAN, WifiNetwork

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ["vlan_id", "name", "description"]


class WifiForm(forms.ModelForm):
    class Meta:
        model = WifiNetwork
        fields = ["ssid", "password"]


class ClientDeviceForm(forms.ModelForm):

    connection_type = forms.ChoiceField(choices=ClientDevice.CONNECTION_TYPES, widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = ClientDevice
        fields = ["name", "mac_address", "ip_address", "wifi", "vlan", "connection_type"]

    def __init__(self, *args, vlan_options=None, wifi_options=None, **kwargs):
        super(ClientDeviceForm, self).__init__(*args, **kwargs)

        self.fields["vlan"].widget = forms.Select(choices=vlan_options, attrs={"class": "form-control"})

        empty_choice = [("", "None")]

        self.fields["wifi"].widget = forms.Select(choices=empty_choice + wifi_options, attrs={"class": "form-control"})
        self.fields["wifi"].required = False
