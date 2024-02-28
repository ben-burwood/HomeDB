import yaml
from django.conf import settings
from django.shortcuts import render


def index(request):
    with open(settings.CONFIG_FILE_PATH, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        if not yaml_data:
            yaml_data = {}
    base_ip = yaml_data.get("base_ip", "0.0")
    router_ip = yaml_data.get("router_ip", "0.0.0.0")

    if request.method == "POST":
        if "base_ip-submit" in request.POST:
            base_ip = request.POST.get("base_ip")
            # Logic for handling Form 1 submission
        elif "router_ip-submit" in request.POST:
            router_ip = request.POST.get("router_ip")
            # Logic for handling Form 2 submission

    return render(request, "ip/index.html", {"base_ip": base_ip, "router_ip": router_ip})
