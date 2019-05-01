from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from .models import Uzytkownik

# Create your views here.
def home(request):
    # tu trzeba pobrac z bazy danych najnowsze elementy
    return render(request,'index/index.html')


def login(request):
    if request.method == 'POST':
        Form= LoginForm(request.POST)
        if Form.is_valid():
            pass
    else:
        Form= LoginForm()
    return render(request,'index/login.html',{'form':Form})


def registration(request):
    if request.method == 'POST':
        Form= RegisterForm(request.POST)
        if Form.is_valid():
            messages.success(request,'udalo sie, form jest dobry')
            NewUser= User(username=Form.data.get('UserName'),password=Form.data.get('Password'),email=Form.data.get('Email'))
            NewUser.save()
            Uzytkownika= Uzytkownik(User=User.objects.get(username=Form.data.get('UserName')),opis_profilu='siemak jestem nowy')
            Uzytkownika.save()
            return redirect('index')
        else:
            messages.success(request,'błąd ostry że ja pierdole, panie jak pan pijany chyba')
            return render(request,'index/registration.html',{'form':Form})
    else:
        Form= RegisterForm()
        return render(request,'index/registration.html',{'form':Form})