from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def assignments(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/assignments.html', {'projects': projects})