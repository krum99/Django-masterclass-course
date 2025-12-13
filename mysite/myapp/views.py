from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return  HttpResponse("Hi")

def item(request):
  return  HttpResponse("<h1>Hi (in h1 tag)</h1>")
