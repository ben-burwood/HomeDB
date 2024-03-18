from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.index, name="index"),
    path("circuit", views.circuit.index, name="circuit.index"),
    path("circuit/create", views.circuit.create, name="circuit.create"),
    path("circuit/<int:id>/edit", views.circuit.edit, name="circuit.edit"),
    path("circuit/<int:id>/delete", views.circuit.delete, name="circuit.delete"),
]
