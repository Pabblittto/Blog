# Generated by Django 2.1.7 on 2019-05-04 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('ID_Bloga', models.IntegerField(primary_key=True, serialize=False)),
                ('Nazwa_Bloga', models.CharField(max_length=128)),
                ('ID_Autora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Komentarz',
            fields=[
                ('ID_Komentarza', models.IntegerField(primary_key=True, serialize=False)),
                ('data_zamieszczenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('tresc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID_Posta', models.IntegerField(primary_key=True, serialize=False)),
                ('Tytul_Posta', models.CharField(max_length=128)),
                ('tresc', models.TextField()),
                ('data_zamieszczenia', models.DateTimeField(default=django.utils.timezone.now)),
                ('haslo', models.CharField(max_length=8)),
                ('obrazek', models.ImageField(upload_to='Obrazki')),
                ('ID_Bloga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zdjecie_profilowe', models.ImageField(default='domyslny_obrazek.jpg', upload_to='Obrazki')),
                ('opis_profilu', models.CharField(max_length=1000)),
                ('uzytkownik', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='komentarz',
            name='ID_Posta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Post'),
        ),
        migrations.AddField(
            model_name='komentarz',
            name='ID_Uzytkownika',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
