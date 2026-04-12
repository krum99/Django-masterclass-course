from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from django.shortcuts import get_object_or_404
from myapp.models import Product 


def cart_add(request):
    cart = Cart(request)
    print("Add to cart button clicked")
    if request.method=="POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to the cart has an id:",product_id)
        print("Product quantity is:",product_quantity)
        #product = Product.objects.get(id=product_id)
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product,product_qty=product_quantity)
        cart_quantity = cart.__len__()
    return JsonResponse({'qty':cart_quantity})

def cart_overview(request):
    cart = Cart(request)
    return render(request, 'cart/cart-overview.html', {'cart': cart})