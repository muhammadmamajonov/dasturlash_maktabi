from django.shortcuts import render
from .models import Playlist
# Create your views here.

def index(request):
    return render(request, 'index.html')


def darslar(request):
    playlistlar = Playlist.objects.all()
    return render(request, 'darslar.html',{'playlistlar':playlistlar})
