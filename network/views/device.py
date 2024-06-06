from django.shortcuts import get_object_or_404, redirect, render

from ..forms import ClientDeviceForm, NetworkDeviceForm
from ..models import ClientDevice, NetworkDevice, VLAN, WifiNetwork

def client_index(request):
    devices = ClientDevice.objects.all()
    return render(request, "network/device/index.html", {"devices": devices})


def network_index(request):
    devices = NetworkDevice.objects.all()
    return render(request, "network/device/index.html", {"devices": devices})


def create_client(request):
    vlan_options = [(vlan.vlan_id, str(vlan)) for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = ClientDeviceForm(request.POST, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("client_device.index")
    else:
        form = ClientDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/create.html", {"form": form})


def create_network(request):
    vlan_options = [(vlan.vlan_id, str(vlan)) for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = NetworkDeviceForm(request.POST, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return NetworkDeviceForm("network_device.index")
    else:
        form = ClientDeviceForm(vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/create.html", {"form": form})


def edit_client(request, id: int):
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

    return render(request, "network/device/edit.html", {"form": form, "device": device})


def edit_network(request, id: int):
    device = get_object_or_404(NetworkDevice, id=id)

    vlan_options = [(vlan.vlan_id, f"{vlan.vlan_id} - {vlan.name}") for vlan in VLAN.objects.all()]
    wifi_options = [(wifi.id, wifi.ssid) for wifi in WifiNetwork.objects.all()]

    if request.method == "POST":
        form = NetworkDeviceForm(request.POST, instance=device, vlan_options=vlan_options, wifi_options=wifi_options)
        if form.is_valid():
            form.save()
            return redirect("device.index")
    else:
        form = NetworkDeviceForm(instance=device, vlan_options=vlan_options, wifi_options=wifi_options)

    return render(request, "network/device/edit.html", {"form": form, "device": device})


def delete_client(request, id: int):
    device = get_object_or_404(ClientDevice, id=id)
    device.delete()
    return redirect("client_device.index")


def delete_network(request, id: int):
    device = get_object_or_404(NetworkDevice, id=id)
    device.delete()
    return redirect("network_device.index")
