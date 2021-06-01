from django.shortcuts import render, redirect
from .models import Playlist, VideoDars
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


def darslar(request):
    playlistlar = Playlist.objects.all()
    return render(request, 'darslar.html',{'playlistlar':playlistlar})

def register(request):
    if request.method == 'POST':
        ism = request.POST['ism']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username olingan")
                messages.info(request, "Username ro'yxatdan o'tkazilgan")
            elif User.objects.filter(email=email).exists():
                print("email olingan")
                messages.info(request, "Bu email ro'yxatdan o'tgan")
            else:
            
                user  = User.objects.create_user(username=username, first_name = ism, email=email, password=password1)
                user.save()
        else:
            print("parol to'g'ri kelmadi")
            messages.info(request, "Parollar bir-biriga to'g'ri kelmadi")
    return render(request, 'register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "username yoki parol hato")
            # User is authenticated
    return render(request, 'login.html')
class PlaylistDateilView(DetailView):
    model = Playlist
    template_name = 'playlist.html'
    context_object_name = 'playlist'


class VideoDarsDetail(DetailView):
    model = VideoDars
    template_name = 'video.html'
    context_object_name = 'video'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['videolar'] = VideoDars.objects.all()
        return context