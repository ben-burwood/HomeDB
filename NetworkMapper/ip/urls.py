from django.urls import path

from . import views

urlpatterns = [
    path("vlan", views.vlan_index, name="vlan.index"),
    path("vlan/create", views.create_vlan, name="vlan.create"),
    path("vlan/<int:vlan_id>/edit", views.edit_vlan, name="vlan.edit"),
    path("vlan/<int:vlan_id>/delete", views.delete_vlan, name="vlan.delete"),
    path("wifi", views.wifi_index, name="wifi.index"),
    path("wifi/create", views.create_wifi, name="wifi.create"),
    path("wifi/<int:id>/edit", views.edit_wifi, name="wifi.edit"),
    path("wifi/<int:id>/delete", views.delete_wifi, name="wifi.delete"),
]
