from common.utils.config import get_config_value, update_config_value
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    if request.method == "POST":
        if "voltage-submit" in request.POST:
            voltage = request.POST.get("voltage")
            update_config_value("voltage", voltage)
            return redirect(reverse("electric_index"))

    voltage = get_config_value("voltage", 0)

    return render(request, "electric/index.html", {"voltage": voltage})
