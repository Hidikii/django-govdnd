from django.shortcuts import render
from .models import Project
import blog

def home(request):
    projects = Project.objects.all() # Добавление в базу данных
    return render(request, 'portfolio/homepage.html', {'projects':projects})

def blog(request):
    return render(request, 'blog/detail.html')
