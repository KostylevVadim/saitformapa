from multiprocessing import context
from django.shortcuts import render
import folium
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {
        'title': 'abcd',
        'tasks': tasks
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def map(request):
    m = folium.Map([132.262, 44.0062], zoom_start=5)
    folium.Marker([132.262, 44.0062],folium.Icon(color='red')).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,

    }
    return render(request, 'main/map.html', context)