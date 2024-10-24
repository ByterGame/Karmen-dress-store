from products.models import Dress, DressCategory
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Karmen Dress',
        'products': Dress.objects.all(),
        'categories': DressCategory.objects.all(),
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'sign_in.html')

def checkout2(request):
    return render(request, 'sign_up.html')

def single_product(request):
    return render(request, 'single-product.html')

