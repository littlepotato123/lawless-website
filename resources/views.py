from django.shortcuts import render
from .models import Resources

# Create your views here.
def all_resources(request):
    events = Resources.objects.all()
    return render(request, 'resources/all_resources.html', {'events': events})