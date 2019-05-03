from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from .models import Uzytkownik, Post, Blog
from django.contrib.auth import views as auth_views


def home(request):
    posts = Post.objects.all()
    blogs = Blog.objects.all()
    users = User.objects.all()
    data = {
        'posts' : posts,
        'blogs' : blogs,
        'users' : users
    }
    if request.user.is_authenticated:
        return render(request,'shared/base.html',data)
    else:
        return render(request,'shared/base.html',data)

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