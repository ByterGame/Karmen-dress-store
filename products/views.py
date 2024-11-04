from lib2to3.fixes.fix_input import context
from products.models import Dress, DressCategory
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Sum
from users.forms import UserShippingForm
from users.models import User
from django.http import JsonResponse
import json

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
        carted_dresses = request.user.cart.all()
        item_count = carted_dresses.count()

        initial_data = {
            'fullname': request.user.fullname,
            'phone': request.user.phone,
            'address': request.user.address,
            'postal_code': request.user.postal_code,
        }

        has_initial_data = all(initial_data.values())
        form = UserShippingForm(initial=initial_data if has_initial_data else None)

        if item_count != 0:
            total_cost = carted_dresses.aggregate(total=Sum('cost'))['total']
            shipping_cost = int(1000/item_count) if int(1000/item_count) > 100 else 0
        else:
            total_cost = 0
            shipping_cost = 0

        result_cost = total_cost + shipping_cost
        context = {
            'carted_dresses': carted_dresses,
            'total_cost': total_cost or 0,
            'shipping_cost': shipping_cost or 0,
            'result_cost': result_cost,
            'form': form,
        'has_initial_data': has_initial_data,
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
    if query:
        products = Dress.objects.filter(
            Q(name__icontains=query) |
            Q(color__icontains=query) |
            Q(model__icontains=query) |
            Q(length__icontains=query)
        )
    else:
        products = Dress.objects.all()

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


def admin_panel(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'admin.html', context)

def admin_dresses(request):
    dresses = Dress.objects.all()
    context = {
        'dresses': dresses,
    }
    return render(request, 'admin_dresses.html', context)


def update_dress(request, id):
    dress = get_object_or_404(Dress, id=id)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dress = Dress.objects.get(pk=id)

            dress.name = data.get('name', dress.name)
            dress.description = data.get('description', dress.description)
            dress.color = data.get('color', dress.color)
            dress.model = data.get('model', dress.model)
            dress.length = data.get('length', dress.length)
            dress.material = data.get('material', dress.material)
            dress.cost = data.get('cost', dress.cost)

            dress.save()  # Сохранение изменений
            return JsonResponse({'success': True})

        except Dress.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Dress not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
