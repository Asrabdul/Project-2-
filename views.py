from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!\nWe've got to home website access!")
def welcome(request):
    return HttpResponse('This is my First Django Welcome Page! Welcome!!!')
