from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse('Contatin')

def about(request):
    return HttpResponse('Sobre nói')
