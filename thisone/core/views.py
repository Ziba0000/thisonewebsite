from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm, LoginForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'categories': categories, 'items': items})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('core:index')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('core:index')
    else:
        form = LoginForm(request)
    return render(request, 'core/login.html', {'form': form})
