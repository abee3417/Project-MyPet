from django.shortcuts import render
from .models import Photo

def index(request):
    return render(request, 'mypet/index.html')

def intro(request):
    return render(request, 'mypet/intro.html')

def daily(request):
    return render(request, 'mypet/daily.html')

def photo(request):
    photo_list = Photo.objects.all()
    context = {'photo_list': photo_list}
    return render(request, 'mypet/photo.html', context)
