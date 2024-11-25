from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm


def home(request):
    photos = Animal.objects.all()
    return render(request, 'home.html', {'photos': photos})


def photo_upload(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm()  # initialize an empty form for GET requests

    # Render the form in both GET and POST (invalid form) cases
    return render(request, 'photo_upload.html', context={'form': form})


def update_photo(request, p_id):
    p = Animal.objects.get(pk=p_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST or None, request.FILES or None, instance=p)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm(instance=p)
        return render(request, 'photo_upload.html', context={'form': form})


def delete_photo(request, p_id):
    Animal.objects.get(pk=p_id).delete()
    return redirect('home')
