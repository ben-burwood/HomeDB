from django import forms

from network.models import Rack, RackItem

class RackForm(forms.ModelForm):

    class Meta:
        model = Rack
        fields = ["name", "width", "rack_units"]

class RackItemForm(forms.ModelForm):

    class Meta:
        model = RackItem
        fields = ["name", "rack_units", "rack", "device"]

    def __init__(self, *args, rack_options=None, device_options=None, **kwargs):
        super(RackItemForm, self).__init__(*args, **kwargs)

        self.fields["rack"].widget = forms.Select(choices=rack_options, attrs={"class": "form-control"})

        self.fields["device"].widget = forms.Select(choices=device_options, attrs={"class": "form-control"})
