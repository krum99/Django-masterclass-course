from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "myapp/index.html", {"products": products})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "myapp/detail.html", {"product": product})
