from django.shortcuts import render, redirect
from .models import Locomotive
from .forms import LocomotiveForm


def index(request):
    locomotives = Locomotive.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'locomotives': locomotives})


def about(request):
    description = Locomotive.objects.all()
    return render(request, 'main/about.html', {'title': 'Описание локомотива', 'description': description})


def create(request):
    error = ''
    if request.method == 'POST':
        form = LocomotiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = LocomotiveForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
