from django.urls import path

from . import views

urlpatterns = [
    path("vlan", views.index, name="vlan.index"),
    path("vlan/create", views.create_vlan, name="vlan.create"),
    path("vlan/<int:vlan_id>/edit", views.edit_vlan, name="vlan.edit"),
]
