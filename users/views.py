from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth, messages
from django.urls import reverse

def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserLoginForm()
    context = {'form' : form}
    return render(request, 'sign_in.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect(reverse('users:sign-in'))
    else:
        form = UserRegisterForm()
    context = {'form' : form}
    return render(request, 'sign_up.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))