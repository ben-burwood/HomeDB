from django.shortcuts import render

from .models import VLAN

def index(request):
    vlans = VLAN.objects.all()
    return render(request, "ip/vlan/index.html", {"vlans": vlans})
