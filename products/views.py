from django.core.management import call_command
from products.models import Dress, DressCategory
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Sum
from users.forms import UserShippingForm
from users.models import User, Order
from yoomoney.models import BalanceChange
from django.http import JsonResponse
import json
from users.forms import DressForm

def index(request):
    liked_dresses = request.user.like.values_list('id', flat=True) if request.user.is_authenticated else []
    carted_dresses = request.user.cart.values_list('id', flat=True) if request.user.is_authenticated else []

    context = {
        'title': 'Karmen Dress',
        'products': Dress.objects.filter(is_available=True),
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
        carted_dresses = request.user.cart.filter(is_available=True)
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

        dresses = list(carted_dresses.values_list('name', flat=True))
        dresses = ', '.join(dresses)
        # item_count = carted_dresses.count()
        #shipping_cost = int(100/item_count)
        result_cost = total_cost + shipping_cost
        context = {
            'carted_dresses': carted_dresses,
            'dresses': dresses,
            'total_cost': total_cost or 0,
            'shipping_cost': shipping_cost or 0,
            'result_cost': result_cost,
            'form': form,
            'has_initial_data': has_initial_data,
            'itemCount': '0',
            'itemSize': '0',

        }
        return render(request, 'cart.html', context)
    else:
        return render(request, 'cart.html')


def likes(request):
    if request.user.is_authenticated:
        carted_dresses = request.user.cart.values_list('id', flat=True)
        context = {
            'liked_dresses': request.user.like.filter(is_available=True),
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
        products = Dress.objects.filter(is_available=True)

    return render(request, 'search.html', {'products': products, 'query': query})


def single_product(request, id):
    dress = get_object_or_404(Dress, id=id)
    all_dresses = Dress.objects.filter(is_available=True)
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
        related_dresses = Dress.objects.filter(id__gt=dress.id, is_available=True).order_by('id')[:3]

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
            dress.save()

            with open('fixtures/Dress.json', 'w', encoding='utf-8') as f:
                call_command('dumpdata', 'products.Dress', format='json', indent=4, stdout=f)

            return JsonResponse({'success': True})

        except Dress.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Dress not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)


def add_dress(request):
    if request.method == 'POST':
        try:
            dress = Dress.objects.create(
                photo=request.POST.get('photo',''),
                photo_hover=request.POST.get('photo_hover',''),
                name=request.POST.get('name',''),
                description=request.POST.get('description',''),
                color=request.POST.get('color',''),
                model=request.POST.get('model',''),
                length=request.POST.get('length',''),
                category_id=request.POST.get('category_id',1),
                material=request.POST.get('material',''),
                cost=request.POST.get('cost',''),
            )
            dress.save()

            with open('fixtures/Dress.json', 'w', encoding='utf-8') as f:
                call_command('dumpdata', 'products.Dress', format='json', indent=4, stdout=f)

            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)

        except Exception as e:
            print("Ошибка:", e)
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)


def orders(request):
    if request.user.is_authenticated:
        user_orders = Order.objects.filter(user_id=request.user.id, is_paid=True)
        orders_with_items = []

        # Проходим по каждому заказу и извлекаем товары
        for order in user_orders:
            items_data = []
            for i,item in enumerate(order.items, start=1):
                try:
                    dress = Dress.objects.get(id=item['id'])
                    items_data.append({
                        'number': i,
                        'dress': dress,
                        'size': item['size'],
                        'quantity': item['quantity'],
                        'total': dress.cost * int(item['quantity'])
                    })
                except Dress.DoesNotExist:
                    # Если товар не найден, пропускаем его
                    continue

            balance_change = BalanceChange.objects.filter(order_id=order.id).last()
            order_date = balance_change.date

            order_status = order.status

            orders_with_items.append({
                'order': order,
                'items': items_data,
                'order_sum': order.order_sum,
                'order_date': order_date,
                'status': order_status,
            })

        context = {
            'orders': orders_with_items,
        }
        return render(request, "orders.html", context)
    else:
        return render(request, "orders.html")


def admin_orders(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        orders_with_items = []

        # Проходим по каждому заказу и извлекаем товары
        for order in orders:
            items_data = []
            for i,item in enumerate(order.items, start=1):
                try:
                    dress = Dress.objects.get(id=item['id'])
                    items_data.append({
                        'number': i,
                        'dress': dress,
                        'size': item['size'],
                        'quantity': item['quantity'],
                        'total': dress.cost * int(item['quantity'])
                    })
                except Dress.DoesNotExist:
                    # Если товар не найден, пропускаем его
                    continue

            balance_change = BalanceChange.objects.filter(order_id=order.id).last()
            order_date = balance_change.date

            order_status = order.status

            orders_with_items.append({
                'order': order,
                'items': items_data,
                'order_sum': order.order_sum,
                'order_date': order_date,
                'status': order_status,
            })

        context = {
            'orders': orders_with_items,
        }
        return render(request, "admin_orders.html", context)
    else:
        return render(request, "admin_orders.html")


def make_available(request, id):
    if request.method == 'POST':
        dress = get_object_or_404(Dress, id=id)
        data = json.loads(request.body)
        is_available = data.get('is_available', dress.is_available)

        dress.is_available = is_available
        dress.save()

        return JsonResponse({'status': 'success', 'message': 'Dress status changed.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


def update_order_status(request,id):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        try:
            order = Order.objects.get(id=order_id)
            order.status = new_status
            order.save()
            return JsonResponse({'status': 'success'})
        except Order.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Заказ не найден'})

    return JsonResponse({'status': 'error', 'message': 'Неверный запрос'})


# def add_dress(request):
#     if request.method == 'POST':
#         form = DressForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'status': 'success', 'message': 'Dress added successfully!'})
#         else:
#             return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)