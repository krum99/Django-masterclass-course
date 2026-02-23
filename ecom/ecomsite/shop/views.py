from django.shortcuts import render
from .models import Product

from django.core.paginator import Paginator

def index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()

    #search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)
    
    #pagination functionality
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/index.html', {'products': page_obj})