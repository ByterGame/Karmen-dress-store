from products.models import Dress, DressCategory
from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'title': 'Karmen Dress',
        'products': Dress.objects.all(),
        'categories': DressCategory.objects.all(),
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')


def single_product(request,  id):
    print(f"Запрошенный ID продукта: {id}")  # Это позволяет увидеть значение ID в консоли
    dress = get_object_or_404(Dress, id=id)
    return render(request, 'single_product.html', {'dress': dress})

