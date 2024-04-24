from django.shortcuts import redirect, render
from django.urls import reverse

from common.utils.config import update_config_value, get_config_value

def index(request):
    if request.method == "POST":
        if "broker_ip-submit" in request.POST:
            broker_ip = request.POST.get("broker_ip")
            update_config_value("broker_ip", broker_ip)
            return redirect(reverse("mqtt_index"))
        elif "broker_port-submit" in request.POST:
            broker_port = request.POST.get("broker_port")
            update_config_value("broker_port", broker_port)
            return redirect(reverse("mqtt_index"))

    broker_ip = get_config_value("broker_ip", "0.0.0.0")
    broker_port = get_config_value("broker_port", "1883")

    return render(request, "mqtt/index.html", {"broker_ip": broker_ip, "broker_port": broker_port})
