from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        ism = request.POST['ism']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('bu username mavjud')
                messages.info(request, "Bu username mavjud")
                return redirect('/acount/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Bu email ro'yxatdan o'tkazilgan")
                return redirect('/acount/register/')
            else:

                user = User.objects.create_user(username=username, first_name=ism, password=password1, email=email)
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Parollar to'g'ri kelmadi")
            return redirect('/acount/register/')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "username yoki parol xato")
            return redirect('/acount/login/')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')