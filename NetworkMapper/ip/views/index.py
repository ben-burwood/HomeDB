import yaml
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse


def update_config_value(key: str, value: str) -> None:
    with open(settings.CONFIG_FILE_PATH, "r+") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file) or {}
        yaml_data[key] = value
        yaml_file.seek(0)
        yaml.dump(yaml_data, yaml_file)
        yaml_file.truncate()


def index(request):
    if request.method == "POST":
        if "base_ip-submit" in request.POST:
            base_ip = request.POST.get("base_ip")
            update_config_value("base_ip", base_ip)
            return redirect(reverse("index"))
        elif "router_ip-submit" in request.POST:
            router_ip = request.POST.get("router_ip")
            update_config_value("router_ip", router_ip)
            return redirect(reverse("index"))

    with open(settings.CONFIG_FILE_PATH, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file) or {}
    base_ip = yaml_data.get("base_ip", "0.0")
    router_ip = yaml_data.get("router_ip", "0.0.0.0")

    return render(request, "ip/index.html", {"base_ip": base_ip, "router_ip": router_ip})
