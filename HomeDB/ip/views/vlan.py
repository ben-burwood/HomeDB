from django.shortcuts import get_object_or_404, redirect, render

from ..forms import VLANForm
from ..models import VLAN


def index(request):
    vlans = VLAN.objects.all()
    return render(request, "ip/vlan/index.html", {"vlans": vlans})


def create(request):
    if request.method == "POST":
        form = VLANForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vlan.index")
    else:
        form = VLANForm()

    return render(request, "ip/vlan/create.html", {"form": form})


def edit(request, vlan_id: int):
    vlan = get_object_or_404(VLAN, vlan_id=vlan_id)

    if request.method == "POST":
        form = VLANForm(request.POST, instance=vlan)
        if form.is_valid():
            form.save()
            return redirect("vlan.index")
    else:
        form = VLANForm(instance=vlan)

    return render(request, "ip/vlan/edit.html", {"form": form, "vlan": vlan})


def delete(request, vlan_id: int):
    vlan = get_object_or_404(VLAN, vlan_id=vlan_id)
    vlan.delete()
    return redirect("vlan.index")
