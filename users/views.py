from django.contrib import messages, auth
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, UserShippingForm
from django.http import JsonResponse
from users.models import User
from products.models import Dress


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

def add_shipping_information(request):
    if request.method == 'POST':
        form = UserShippingForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Shipping information added successfully!'})
        else:
            messages.error(request, "Please correct the errors below.")
            return JsonResponse({'status': 'error', 'errors': form.errors, 'message': 'Please correct the errors below.'} )

    return JsonResponse({'status': 'error', 'errors': {'__all__': ['Invalid request method.']}, 'message': 'Please correct the errors below.'})