from django.shortcuts import render, get_object_or_404, redirect
from .models import State, Place
from .forms import StateForm, PlaceForm


def create_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_list')
    else:
        form = StateForm()
    return render(request, 'create_state.html', {'form': form})


def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, 'create_place.html', {'form': form})


def state_list(request):
    states = State.objects.all()
    return render(request, 'state_list.html', {'states': states})


def student_list(request):
    places = Place.objects.all()
    return render(request, 'place_list.html', {'Places': places})


def update_state(request, pk):
    state = get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_list')
    else:
        form = StateForm(instance=state)
    return render(request, 'update_state.html', {'form': form})


def update_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm(instance=place)
    return render(request, 'update_place.html', {'form': form})


def delete_state(request, pk):
    state = get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        state.delete()
        return redirect('state_list')
    return render(request, 'delete_state.html', {'state': state})


def delete_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('place_list')
    return render(request, 'delete_place.html', {'place': place})