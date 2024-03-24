from django.shortcuts import render
from .models import Products

def shop_page(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "./shop_page.html", context)
