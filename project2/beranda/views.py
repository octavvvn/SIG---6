from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Selamat Datang di Halaman Beranda.")

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html') 
# Create your views here.

from .models import Provinsi,NamaData, Datprof
def peta_provinsi(request):
    
    # Ambil semua data provinsi dari database
    data_provinsi = Provinsi.objects.all()
    # Ambil semua data nama data dari database
    data_namadata = NamaData.objects.all()
    return render(request, 'peta_provinsi.html',{
        'data_provinsi': data_provinsi,
        'data_namadata': data_namadata,
    })