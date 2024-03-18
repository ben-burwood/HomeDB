from django.shortcuts import get_object_or_404, redirect, render

from ..forms import CircuitForm
from ..models.circuits import Circuit

def index(request):
    circuits = Circuit.objects.all()
    return render(request, "electric/circuit/index.html", {"circuits": circuits})


def create(request):
    if request.method == "POST":
        form = CircuitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("circuit.index")
    else:
        form = CircuitForm()

    return render(request, "electric/circuit/create.html", {"form": form})


def edit(request, id: int):
    circuit = get_object_or_404(Circuit, id=id)

    if request.method == "POST":
        form = CircuitForm(request.POST, instance=circuit)
        if form.is_valid():
            form.save()
            return redirect("circuit.index")
    else:
        form = CircuitForm(instance=circuit)

    return render(request, "electric/circuit/edit.html", {"form": form, "circuit": circuit})


def delete(request, id: int):
    circuit = get_object_or_404(Circuit, id=id)
    circuit.delete()
    return redirect("circuit.index")
