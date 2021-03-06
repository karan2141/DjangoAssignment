from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import UserLoginForm, RegisterForm

def oauth(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password= password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'login.html', {'form': form})

def register_view(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username= user.username, password= password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')