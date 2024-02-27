from django.shortcuts import get_object_or_404, redirect, render

from ..forms import WifiForm
from ..models import WifiNetwork

def index(request):
    wifis = WifiNetwork.objects.all()
    return render(request, "ip/wifi/index.html", {"wifis": wifis})


def create(request):
    if request.method == "POST":
        form = WifiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wifi.index")  # Redirect to the VLAN Index after successful creation
    else:
        form = WifiForm()

    return render(request, "ip/wifi/create.html", {"form": form})


def edit(request, id: int):
    wifi = get_object_or_404(WifiNetwork, id=id)

    if request.method == "POST":
        form = WifiForm(request.POST, instance=wifi)
        if form.is_valid():
            form.save()
            return redirect("wifi.index")  # Redirect to the VLAN Index after successful edit
    else:
        form = WifiForm(instance=wifi)

    return render(request, "ip/wifi/edit.html", {"form": form, "wifi": wifi})


def delete(request, id: int):
    wifi = get_object_or_404(WifiNetwork, id=id)
    wifi.delete()
    return redirect("wifi.index")
