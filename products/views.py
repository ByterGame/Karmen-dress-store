from products.models import Dress, DressCategory
from django.shortcuts import render, get_object_or_404

def index(request):
    liked_dresses = request.user.like.values_list('id', flat=True) if request.user.is_authenticated else []
    carted_dresses = request.user.cart.values_list('id', flat=True) if request.user.is_authenticated else []
    context = {
        'title': 'Karmen Dress',
        'products': Dress.objects.all(),
        'categories': DressCategory.objects.all(),
        'liked_dresses': liked_dresses,
        'carted_dresses': carted_dresses,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    if request.user.is_authenticated:
        context = {
            'carted_dresses': request.user.cart.all(),
        }
        return render(request, 'cart.html', context)
    else:
        return render(request, 'cart.html')


def likes(request):
    if request.user.is_authenticated:
        carted_dresses = request.user.cart.values_list('id', flat=True)
        context = {
            'liked_dresses': request.user.like.all(),
            'carted_dresses': carted_dresses,
        }
        return render(request, 'likes.html', context)
    else:
        return render(request, 'likes.html')


def search(request):
    query = request.GET.get('query', '')
    products = Dress.objects.filter(name__icontains=query) if query else Dress.objects.all()
    return render(request, 'search.html', {'products': products, 'query': query})


def single_product(request, id):
    dress = get_object_or_404(Dress, id=id)
    all_dresses = Dress.objects.order_by('id')
    liked_dresses = request.user.like.values_list('id', flat=True) if request.user.is_authenticated else []
    carted_dresses = request.user.cart.values_list('id', flat=True) if request.user.is_authenticated else []

    current_index = list(all_dresses.values_list('id', flat=True)).index(dress.id)

    if current_index == len(all_dresses) - 1:
        related_dresses = all_dresses[:3]
    elif current_index == len(all_dresses) - 2:
        related_dresses = list(all_dresses[current_index + 1:]) + list(all_dresses[:2])
    elif current_index == len(all_dresses) - 3:
        related_dresses = list(all_dresses[current_index + 1:]) + list(all_dresses[:1])
    else:
        related_dresses = Dress.objects.filter(id__gt=dress.id).order_by('id')[:3]

    context = {'dress': dress,
        'related_dresses': related_dresses,
        'liked_dresses': liked_dresses,
        'carted_dresses': carted_dresses,
    }
    return render(request, 'single_product.html', context)