from django.shortcuts import redirect, render

from .forms import VLANForm
from .models import VLAN


def index(request):
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
