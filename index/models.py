from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Blog(models.Model):
    ID_Bloga=models.IntegerField(primary_key=True)
    Nazwa_Bloga=models.CharField(max_length=128)
    ID_Autora=models.ForeignKey(User,on_delete=models.CASCADE)

class Post(models.Model):
    ID_Posta=models.IntegerField(primary_key=True)
    Tytul_Posta=models.CharField(max_length=128)
    tresc=models.TextField()
    data_zamieszczenia=models.DateTimeField(default=timezone.now)
    ID_Bloga=models.ForeignKey(Blog,on_delete=models.CASCADE)
    haslo=models.CharField(max_length=8)
    obrazek=models.ImageField(upload_to='Obrazki')

class Uzytkownik(models.Model):
    uzytkownik=models.OneToOneField(User,on_delete=models.CASCADE) #dziedziczenie pola z wbudowanej tabeli User
    zdjecie_profilowe=models.ImageField(default='domyslny_obrazek.jpg',upload_to='Obrazki')
    opis_profilu=models.CharField(max_length=1000)

class Komentarz(models.Model):
    ID_Komentarza=models.IntegerField(primary_key=True)
    ID_Uzytkownika=models.ForeignKey(User,on_delete=models.CASCADE)
    ID_Posta=models.ForeignKey(Post,on_delete=models.CASCADE)
    data_zamieszczenia=models.DateTimeField(default=timezone.now)
    tresc=models.TextField()


