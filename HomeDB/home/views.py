from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")


def settings(request):
    raise NotImplementedError("Settings page not implemented yet")
    return render(request, "home/settings.html")