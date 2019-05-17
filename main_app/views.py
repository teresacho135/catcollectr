from django.shortcuts import render
from .models import Cat

# Create your views here.
def index(request): 
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})
