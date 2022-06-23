from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

# Create your views here.

def ahoj(request):
    return HttpResponse('<h1>Ahoj, sekai!</h1>')