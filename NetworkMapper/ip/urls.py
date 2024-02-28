from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.index, name="index"),
    path("vlan", views.vlan.index, name="vlan.index"),
    path("vlan/create", views.vlan.create, name="vlan.create"),
    path("vlan/<int:vlan_id>/edit", views.vlan.edit, name="vlan.edit"),
    path("vlan/<int:vlan_id>/delete", views.vlan.delete, name="vlan.delete"),
    path("wifi", views.wifi.index, name="wifi.index"),
    path("wifi/create", views.wifi.create, name="wifi.create"),
    path("wifi/<int:id>/edit", views.wifi.edit, name="wifi.edit"),
    path("wifi/<int:id>/delete", views.wifi.delete, name="wifi.delete"),
    path("device", views.device.index, name="device.index"),
    path("device/create", views.device.create, name="device.create"),
    path("device/<int:id>/edit", views.device.edit, name="device.edit"),
    path("device/<int:id>/delete", views.device.delete, name="device.delete"),
]
