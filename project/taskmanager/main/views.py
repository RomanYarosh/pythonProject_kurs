from django.shortcuts import render, redirect, get_object_or_404
from .models import Locomotive
from .forms import LocomotiveForm


def index(request):
    locomotives = Locomotive.objects.all()
    return render(request, 'main/index.html', {'title': 'Каталог локомотивов', 'locomotives': locomotives})


def about(request, locomotive_id):
    locomotive = get_object_or_404(Locomotive, id=locomotive_id)
    print(locomotive)
    return render(request, 'main/about.html', {'title': 'Описание локомотива', 'locomotive': locomotive})


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
