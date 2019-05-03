from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns= [
    path('login/',auth_views.LoginView.as_view(), name='Login'),
    path('registration/',views.registration,name='registration'),
    path('',views.home,name='index'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/',views.profile, name='profile')
]