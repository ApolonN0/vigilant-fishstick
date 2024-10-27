from django.shortcuts import render
from shop.models import Product

# Create your views here.
def catalog(request):
    products  = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products}) 
def create_order(request):
    return render(request, 'shop/create_order.html')
def orders (request):
    return render(request, 'shop/orders.html')
def product_details(request):
    return render(request, 'shop/product_details.html')