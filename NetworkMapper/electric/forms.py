from django import forms

from .models.circuits import Circuit

class CircuitForm(forms.ModelForm):

    breaker_type = forms.ChoiceField(choices=Circuit.BREAKER_TYPES, widget=forms.Select(attrs={"class": "form-control"}))
    circuit_type = forms.ChoiceField(choices=Circuit.CIRCUIT_TYPES, widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Circuit
        fields = ["name", "current_rating", "breaker_type", "spd_protection", "wire_diameter", "circuit_type", "description"]
