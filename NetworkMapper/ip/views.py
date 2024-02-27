from django.shortcuts import get_object_or_404, redirect, render

from .forms import VLANForm, WifiForm
from .models import VLAN, WifiNetwork

def vlan_index(request):
    vlans = VLAN.objects.all()
    return render(request, "ip/vlan/index.html", {"vlans": vlans})


def create_vlan(request):
    if request.method == "POST":
        form = VLANForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vlan.index")  # Redirect to the VLAN Index after successful creation
    else:
        form = VLANForm()

    return render(request, "ip/vlan/create.html", {"form": form})


def edit_vlan(request, vlan_id: int):
    vlan = get_object_or_404(VLAN, vlan_id=vlan_id)

    if request.method == "POST":
        form = VLANForm(request.POST, instance=vlan)
        if form.is_valid():
            form.save()
            return redirect("vlan.index")  # Redirect to the VLAN Index after successful edit
    else:
        form = VLANForm(instance=vlan)

    return render(request, "ip/vlan/edit.html", {"form": form, "vlan": vlan})


def wifi_index(request):
    wifis = WifiNetwork.objects.all()
    return render(request, "ip/wifi/index.html", {"wifis": wifis})


def create_wifi(request):
    if request.method == "POST":
        form = WifiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wifi.index")  # Redirect to the VLAN Index after successful creation
    else:
        form = WifiForm()

    return render(request, "ip/wifi/create.html", {"form": form})


def edit_wifi(request, id: int):
    wifi = get_object_or_404(WifiNetwork, id=id)

    if request.method == "POST":
        form = WifiForm(request.POST, instance=wifi)
        if form.is_valid():
            form.save()
            return redirect("wifi.index")  # Redirect to the VLAN Index after successful edit
    else:
        form = WifiForm(instance=wifi)

    return render(request, "ip/wifi/edit.html", {"form": form, "wifi": wifi})
