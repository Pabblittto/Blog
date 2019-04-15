from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # tu trzeba pobrac z bazy danych najnowsze elementy
    return render(request,'index/index.html')