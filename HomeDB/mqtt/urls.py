from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.index, name="mqtt_index"),
]
