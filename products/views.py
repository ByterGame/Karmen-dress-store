from products.models import Dress, DressCategory
from django.shortcuts import render

def products(request):
    context = {
        'title': 'Karmen Dress',
        'products': Dress.objects.all(),
        'categories': DressCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
