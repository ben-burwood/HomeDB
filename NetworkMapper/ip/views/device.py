from django.shortcuts import get_object_or_404, redirect, render

from ..forms import ClientDeviceForm
from ..models import ClientDevice, VLAN, WifiNetwork

def index(request):
    devices = ClientDevice.objects.all()
    return render(request, "ip/device/index.html", {"devices": devices})


def create(request):
    vlan_options = [(vlan.vlan_id, str(vlan)) for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = ClientDeviceForm(request.POST, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("device.index")
    else:
        form = ClientDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "ip/device/create.html", {"form": form})


def edit(request, id: int):
    device = get_object_or_404(ClientDevice, id=id)

    vlan_options = [(vlan.vlan_id, f"{vlan.vlan_id} - {vlan.name}") for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = ClientDeviceForm(request.POST, instance=device, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("device.index")
    else:
        form = ClientDeviceForm(instance=device, vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "ip/device/edit.html", {"form": form, "device": device})


def delete(request, id: int):
    device = get_object_or_404(ClientDevice, id=id)
    device.delete()
    return redirect("device.index")
