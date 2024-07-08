from django import forms

from network.models import ClientDevice, NetworkDevice
from network.models.device import InfrastructureDevice, NetworkedDevice
from network.objects import ConnectionType

class NetworkedDeviceForm(forms.ModelForm):

    connection_type = forms.ChoiceField(
        choices=ConnectionType.choices(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = NetworkedDevice
        abstract = True
        fields = [
            "name",
            "mac_address",
            "vlan",
            "ip_address",
            "connection_type",
            "wifi",
        ]

    def __init__(self, *args, vlan_options=None, wifi_options=None, **kwargs):
        super(NetworkedDeviceForm, self).__init__(*args, **kwargs)

        self.fields["vlan"].widget = forms.Select(choices=vlan_options, attrs={"class": "form-control"})

        empty_choice = [("", "None")]

        self.fields["wifi"].widget = forms.Select(choices=empty_choice + wifi_options, attrs={"class": "form-control"})
        self.fields["wifi"].required = False

    def clean(self):
        cleaned_data = super().clean()

        connection_type = cleaned_data.get("connection_type")
        wifi = cleaned_data.get("wifi")
        if connection_type == "ethernet" and wifi:
            raise forms.ValidationError("WiFi must be null for Ethernet Connections", code="invalid")
        if connection_type == "wifi" and not wifi:
            raise forms.ValidationError("WiFi must be set for WiFi Connections", code="invalid")

        return cleaned_data


class ClientDeviceForm(NetworkedDeviceForm):
    class Meta(NetworkedDeviceForm.Meta):
        model = ClientDevice


class NetworkDeviceForm(NetworkedDeviceForm):
    class Meta(NetworkedDeviceForm.Meta):
        model = NetworkDevice
        fields = NetworkedDeviceForm.Meta.fields + ["device_type"]


class InfrastructureDeviceForm(forms.ModelForm):
    class Meta:
        model = InfrastructureDevice
        fields = ["name", "device_type"]
