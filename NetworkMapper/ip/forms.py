from django import forms

from .models import VLAN

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ["vlan_id", "name", "description"]
