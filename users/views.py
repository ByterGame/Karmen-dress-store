from django.contrib import messages, auth
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from yoomoney.payment import create_payment
from .forms import UserLoginForm, UserRegisterForm, UserShippingForm
from django.http import JsonResponse, HttpResponse
from users.models import User, Order
from products.models import Dress
import json
import json


def sign_in(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return JsonResponse({'status': 'success', 'message': 'You successfully logged in.'})
            else:
                return JsonResponse({'status': 'error', 'errors': {'username': ['Invalid login or password.']}})
        else:
            return JsonResponse({'status': 'error', 'errors': {'username': form.errors['__all__']}})
    return JsonResponse({'status': 'error', 'errors': {'username': ['Invalid request method.']}})


def sign_up(request):
    form = UserRegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account created successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'errors': {'__all__': ['Invalid request method.']}})


def logout(request):
    auth.logout(request)
    referer_url = request.META.get('HTTP_REFERER', 'products:index')
    return HttpResponseRedirect(referer_url)


def add_to_cart(request):
    if request.user.is_authenticated:
        dress_id = request.POST.get('dress_id')
        dress = get_object_or_404(Dress, id=dress_id)
        if dress in request.user.cart.all():
            request.user.cart.remove(dress)
            return JsonResponse({'status': 'removed', 'message': 'Product removed from cart.'})
        else:
            request.user.cart.add(dress)
            return JsonResponse({'status': 'success', 'message': 'Product added successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Please login first.'})


def add_to_likes(request):
    if request.user.is_authenticated:
        dress_id = request.POST.get('dress_id')
        dress = get_object_or_404(Dress, id=dress_id)
        if dress in request.user.like.all():
            request.user.like.remove(dress)
            return JsonResponse({'status': 'removed', 'message': 'Product removed from likes.'})
        else:
            request.user.like.add(dress)
            return JsonResponse({'status': 'success', 'message': 'Product added successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Please login first.'})


def remove_from_cart(request):
    dress_id = request.POST.get('dress_id')
    dress = get_object_or_404(Dress, id=dress_id)
    request.user.cart.remove(dress)
    return JsonResponse({'status': 'removed', 'message': 'Product removed from cart.'})


def remove_from_likes(request):
    dress_id = request.POST.get('dress_id')
    dress = get_object_or_404(Dress, id=dress_id)
    request.user.like.remove(dress)
    return JsonResponse({'status': 'removed', 'message': 'Product removed from likes.'})


@csrf_exempt
def add_shipping_information(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'errors': {'__all__': ['Invalid request method.']},
                             'message': 'Please correct the errors below.'})
    data = json.loads(request.body)

    if len(data['items']) == 0:
        return HttpResponse(status=502)
    order = Order(user=request.user, items=data['items'],)
    order.shipping_info = dict(address=data["address"],
                                          fullname = data["fullname"],
                                          postal_code = data["postal_code"],
                                          phone = data["phone"])
    order.calculate_order_sum()
    order.save()
    request.user.address = data["address"]
    request.user.fullname = data["fullname"]
    request.user.postal_code = data["postal_code"]
    request.user.phone = data["phone"]
    request.user.save()

    confirmation_url = create_payment(request.user.id, order)
    request.user.cart.clear()

    return JsonResponse(dict(url_to_redirect=confirmation_url, status='success'))


def make_superuser(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=id)
        data = json.loads(request.body)
        is_superuser = data.get('is_superuser', user.is_superuser)

        user.is_superuser = is_superuser
        user.save()

        return JsonResponse({'status': 'success', 'message': 'Admin status changed.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
