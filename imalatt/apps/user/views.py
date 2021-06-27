from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import User


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home:kapilar')

    return render(request, "loginform.html", {"form": form, 'title': 'Giriş Yap', })


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home:home')
    else:
        return redirect('home:401')
